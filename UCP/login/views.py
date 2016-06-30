"""
Views file for Login App

contains views for the frontend pages of the Login App
"""

from django.contrib.auth import logout as django_logout
from django.shortcuts import render, redirect
from django.views.generic import View

from login.functions import login, register, forgot_password, reset_password, get_response_text, get_user_details, update_profile, get_user_profile
from UCP.constants import result
from UCP.functions import get_base_context

class Login(View):
    
    def get(self, request):
        context = {}
        context["is_login_page"] = True
        
        if request.user.is_authenticated():
            context = get_base_context(request)
            return render(request, 'home.html', context)
            
        return render(request, 'login-register.html', context)
        
        response = login(request)
        
        if response["result"] == result.RESULT_SUCCESS:
            context = get_base_context(request)
            return render(request, 'home.html', context)
        else:
            context["message"] = get_response_text(response)
        
            return render(request, 'login-register.html', context)
    
    def post(self, request):
        context = {}
        context["is_login_page"] = True
        
        if request.user.is_authenticated():
            context = get_base_context(request)
            return render(request, 'home.html', context)
        
        response = login(request)
        
        if response["result"] == result.RESULT_SUCCESS:
            context = get_base_context(request)
            return render(request, 'home.html', context)
        else:
            context["message"] = get_response_text(response)
        
            return render(request, 'login-register.html', context)


class Logout(View):
    
    def get(self, request):
        
        django_logout(request)
        return redirect('/user/login')


class Register(View):
    
    def get(self, request):
        return render(request, 'login-register.html')
        
    def post(self, request):

        context={}
        
        response = register(request)
        
        context["message"] = get_response_text(response)
        
        return render(request, 'login-register.html', context)
        

class ForgotPassword(View):
    
    def get(self, request):
        
        context={}
        response = forgot_password(request)
        context["message"] = get_response_text(response)
        
        if(response["result"] == 0):
            context["is_login_page"] = True
            print context
            return render(request, 'login-register.html', context)
        if(response["result"] == 1):
            return render(request, 'reset-password.html', context)
       

class ResetPassword(View):

   def post(self, request):

       context={}
       response = reset_password(request)
       context["message"] = get_response_text(response)

       if(response["result"] == 1):
           context["is_login_page"] = True
           return render(request, 'login-register.html', context)
       if(response["result"] == 0):
           return render(request, 'reset-password.html', context)
    
        
class EditProfile(View):
    
    def get(self, request):
        
        context={}
        
        context['user'] = get_user_details(request)
        print context
        
        return render(request, 'edit-profile.html', context)
    
    def post(self, request):
        context={}
        
        response = update_profile(request)
        context['user'] = get_user_details(request)
        context["response"] = response
        
        return render(request, 'edit-profile.html', context)
    
        
class Profile(View):
    
    def get(self, request, pk):
        
        context={}
        
        context['user'] = get_user_profile(pk)
        
        return render(request, 'profile.html', context)
    
        
        
        
        
        
