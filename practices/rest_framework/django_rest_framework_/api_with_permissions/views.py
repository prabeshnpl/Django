from rest_framework.views import APIView,Response ,status
from .models import Users
from .serializer import UserSerializer,LoginSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated,AllowAny

class UserApiView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        elif self.request.method == "POST":
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self,request):
        if request.user.is_authenticated and "logged_in" not in request.session:
            logout(request)

        print(request.user)
        queryset = Users.objects.all()
        if queryset :
            serializer = UserSerializer(queryset,many=True)
            return Response(serializer.data)
        else:
            return Response({"message":"No data"},status=status.HTTP_204_NO_CONTENT)

    def post(self,request):
        if request.user.is_authenticated and "logged_in" not in request.session:
            logout(request)

        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':{'message':'Created successfully'}},status=status.HTTP_201_CREATED)
        else:
            return Response({'data':{'error':serializer.errors}},status=status.HTTP_406_NOT_ACCEPTABLE)

class LoginAPI(APIView):

    def get(self,request):

        if request.user.is_authenticated and "logged_in" not in request.session:
            logout(request)

        return Response({
            "message":"Enter 'username' and 'password' to login",
        })

    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({'Error':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
        username = serializer.data['username']
        password = serializer.data['password']
        
        user_obj = authenticate(username=username,password=password)
        if user_obj:
            login(request,user_obj)
            if "logged_in" not in request.session:
                request.session["logged_in"]=True
            return Response({"message":"Logged in successfully."},status=status.HTTP_202_ACCEPTED)
        
        return Response({"message":"Invalid User. User not found."},status=status.HTTP_404_NOT_FOUND)


# user_sessions = Session.objects.filter(expire_date__gte=now())
# user_ids = user_sessions.values_list('_auth_user_id', flat=True)  # Fetch user IDs from sessions
# print("User IDs in active sessions:", user_ids)

# # For a specific user
# specific_user_sessions = user_sessions.filter(_auth_user_id=str(user.id))
# print("Specific User Sessions:", specific_user_sessions)
# for session in specific_user_sessions:
#     session.delete()