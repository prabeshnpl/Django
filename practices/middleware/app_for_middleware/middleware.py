from datetime import datetime
from django.http import HttpResponse
import copy 
from django.utils.deprecation import MiddlewareMixin

class MaintainenceMiddleWare:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if datetime.now().hour == 8 and datetime.now().minute == 5:
            # print("Content blocked")
            response = HttpResponse("Sorry under maintainence")
            # print("Sorry you can't access")
        else:
            # print("You are here at right time.")
            response = self.get_response(request)
            # print("Response generated.")

        return response


class MiddleWare(MiddlewareMixin):

    def __init__(self, get_response):
        # print("one time intitalization")
        self.get_response = get_response
        self.allowed = ['127.0.0.1',]

    def __call__(self, request, *args, **kwds):
        # print(request.META.get('REMOTE_ADDR'))

        if request.META.get('REMOTE_ADDR') not in self.allowed:
            # request.META['Custom_header'] = 'Unverified'
            print("Sorry your IP is blocked.")
            # response =  HttpResponse('Sorry your IP is blocked')
        else:
            # print("Before the View")
            request.META['Custom_header'] = 'Verified'
            response = self.get_response(request)
            # print("After the view")

        return response

    def process_request(self, request):
        """ Called after every request before view is called. Used to process the request only."""

        if 'block' in request.path:
            return HttpResponse("Blocked!")  # Skip the view

    def process_view(self, request, view_func, view_args, view_kwargs):
        """ Called just before rendering requested view . Can inspect or modify the arguments of view func. E.g. auntentication"""

        if not request.user.is_authenticated:
            return HttpResponse("Authentication required!")
    
    def process_template_response(self, request, response):
        """ Called if the response is a TemplateResponse.
            Can modify the context or template before rendering. """
        new_context_data = copy.copy(response.context_data)
        print(new_context_data['username'])
        new_context_data['additional_message'] = 'Hello from middleware!'
        response.context_data = new_context_data 
        return response
        
    def process_response(self,request,response):
        """ Called after view has been processed and response has been generated. 
        Called after every response """

        if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
            print('Yep we got in here')
            if request.POST['username'] == 'admin' and request.POST['password'] == 'admin':
                if 'text/html' in response['Content-Type']:
                    response.content = response.content.replace(b'admin',b'Welcome boss')
            return response
        
        # print("Middleware hit") 
        # if request.method == 'POST': 
        #     print("It's a POST request") 
        #     if 'username' in request.POST and 'password' in request.POST:
        #         print("Username and password in POST data") 
        #         if request.POST['username'] == 'admin' and request.POST['password'] == 'admin':
        #             print("Admin credentials matched")
        #             if 'text/html' in response['Content-Type']:
        #                     print("Response is HTML") 
        #                     response.content = response.content.replace(b'admin', b'Welcome boss')
        #                     return response
    
    def process_exception(self, request, exception):
        """ Called when exception is raised during execution """

        print(f"Exception occurred: {exception}")
        return HttpResponse("Something went wrong!")
    
    



    