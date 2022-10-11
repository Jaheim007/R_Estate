from django.shortcuts import render , redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib import messages #import messages

from Property import forms
from Property import models

class Property(View):
    template_name = 'page/properties.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Single(View):
    template_name = 'page/property-single.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class AddProperty(View):
    template_name = 'page/add_property.html'
    add_form = forms.AddProperty
    
    def get(self , request):
        form = self.add_form
        return render(request , self.template_name , locals())
    
    def post(self , request):
        msg =''
        success = True
        
        name = request.POST.get("name")
        price = request.POST.get("price")
        status = request.POST.get('status')
        address_name = request.POST.get('address_name')
        property_type = request.POST.get('property_type')
        description = request.POST.get('description')
        bedroom = request.POST.get("bedroom")
        bathroom = request.POST.get("bathroom")
        garage = request.POST.get("garage")
        main_image = request.POST.get("main_image")
        users = request.user
        
        instance_bedroom = models.Bedrooms.objects.get(pk=bedroom)
        instance_bathroom = models.Bathrooms.objects.get(pk=bathroom)
        instance_garage = models.Garages.objects.get(pk=garage)
        instance_type_property = models.TypeProperty.objects.get(pk=property_type)
            
         
        property = models.Properties(
            name = name, 
            price = price,
            status = status,
            address_name = address_name,
            property_type = instance_type_property,
            description = description , 
            bedroom = instance_bedroom, 
            bathroom = instance_bathroom, 
            garage = instance_garage, 
            main_image = main_image,
            users = users
        )
        
        property.save()
        
        msg = 'Your email has been saved, we will keep you updated on our latest info.'
        
        data = {
        'msg': msg,
        'success': success
        }
        
        return redirect("myproperty")
