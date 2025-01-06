from rest_framework import generics,status
from .models import Items
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import ItemSerializers
# Create your views here.

# class ItemListCreate(generics.ListCreateAPIView):
#     serializer_class = ItemSerializers
#     queryset = Items.objects.all()

#     def delete(self,request,*args,**kwargs):
#         Items.objects.all().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ItemCRUD(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ItemSerializers
#     queryset = Items.objects.all()
#     lookup_field ='pk'

class ItemAPI(APIView):
    def get(self,request,pk=None):

        if pk:
            try:
                item = Items.objects.get(pk=pk)
                serializer = ItemSerializers(item)
                return Response(serializer.data)
            except Items.DoesNotExist:
                return Response({f'Item with id {pk} not found'},status=status.HTTP_404_NOT_FOUND)

        else:
            item = Items.objects.all()

        serializer = ItemSerializers(item,many=True)

        return Response(serializer.data)

    def delete(self,request,pk=None):
        if pk:
            try:
                item= Items.objects.get(pk=pk)
                item.delete()
                return Response({'message':'Item Deleted Successfully'},status=status.HTTP_204_NO_CONTENT)
            except Items.DoesNotExist:
                return Response({'message':'Item Not found'},status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({'message':'Provide Id to delete'},status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        serializer = ItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if pk:
            try:
                item = Items.objects.get(pk=pk)
                serializer = ItemSerializers(item, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Items.DoesNotExist:
                return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response({"error": "Provide an ID to update an item"}, status=status.HTTP_400_BAD_REQUEST)




            


    