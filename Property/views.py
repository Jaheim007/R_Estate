from django.shortcuts import render , redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib import messages #import messages

from Property import forms
from Property import models

class Property(View):
    template_name = 'page/properties.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Single(View):
    template_name = 'page/property-single.html'
    
    def get(self , request , details):
        property = models.Properties.objects.get(id=details)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class AddProperty(View):
    template_name = 'page/add_property.html'
    add_form = forms.AddPropertyForm
    
    def get(self , request):
        form = self.add_form()   
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.add_form(request.POST , request.FILES )
        
        if form.is_valid():
    
            show=form.save(commit=False)
            
            show.users = request.user
            
            show.save()
            messages.success(request, "Property Updated.")
            return redirect("view_property")
        return redirect("add_property")
    
class ViewProperty(View):
    template_name = 'page/view_property.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
        
        
        
        
        
        
        
        
        
        
        
        

