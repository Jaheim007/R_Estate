from django.contrib.auth import get_user_model
from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm , PasswordResetForm
from django.contrib import messages #import messages

from Authentication import forms

class Login(View):
    template_name = 'page/login.html'
    classe = forms.LoginUserForm
    
    def get(self , request):
        form = self.classe
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.classe(request.POST)
        if form.is_valid():     
            user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"]
            )
        if user:
            login(request, user)
            return redirect("home") 
        
        return render(request , self.template_name , locals())
    
class SignUp(View):
    template_name = 'page/signup.html'
    classe = forms.NewUserForm
    
    def get(self,request):
        form = self.classe
        return render(request,self.template_name,locals())
    
    def post(self,request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        
        user = get_user_model().objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email = email, 
                password = password1, 
        )

        messages.success(request, "Account successfully created." )
        user.save()
        return redirect("login")
    
class Logout(View):
    
    def get(self , request):
       logout(request)
       return redirect("/") 
   

class Profile(View):
    template_name = 'page/profile.html'
    
    def get(self,request):
        return render(request, self.template_name , locals())
    
    def post(self,request):
        pass
    
class EditProfile(View):
    template_name = 'page/edit_profile.html'
    classe = forms.EditUserProfile
    
    def get(self, request):
        form = self.classe(instance=request.user)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.classe(request.POST , request.FILES , instance=request.user)
        
        if form.is_valid():
            messages.success(request, "Account Updated." )
            form.save()
            return redirect("profile")
        return redirect("edit")
    

    



    


