from django.shortcuts import render , redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib import messages #import messages
from django.db.models import Q 
from django.http import JsonResponse

from Property import forms
from Property import models
from Authentication import models as auth


class Property(View):
    template_name = 'page/properties.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Single(View):
    template_name = 'page/property-single.html'
    
    def get(self , request ,details):
        property = models.Properties.objects.get(id=details)
        c = models.Properties.objects.get(id=details)
        return render(request , self.template_name , locals())
    
    def post(self , request, details):
        usered = models.Properties.objects.get(id=details)
        msg =''
        success = True
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            save_user = usered.users
            
            mail = auth.User.objects.get(username=save_user)
            mail_email = mail.email
            print(save_user)
            
            request_time = models.RequestTime(
                name = name , 
                email = email, 
                subject = subject, 
                message = message,
                save_user = save_user
            )
            
            
        request_time.save()
        send_mail(
                "Konato Account",
                "Your seller's account was created with success. ",
                'jaheimkouaho@gmail.com',
                [mail_email],
                fail_silently=False
        )
        
        msg = 'Thank you for contacting Medicio.'
            
        data = {
            'msg': msg,
            'success': success
        }

        return redirect('single_property', usered.id)

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
    
class SearchProperty(View):
    template_name = 'page/search.html'
    
    def get(self , request):
        results = []
        
        if request.method == "GET":
        
            query = request.GET.get('search')

            if query == '':

                query = 'None'
                messages.error(request, "No Properties in that location.")
                
                print(query)

            results = models.Properties.objects.filter(Q(location__city=query))
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class EditProperty(View):
    template_name = 'page/edit_property.html'
    classe = forms.EditPropertyForm
    
    def get(self, request):
        form = self.classe(instance=request.Properties)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.classe(request.POST , request.FILES , instance=request.Properties)
        
        if form.is_valid():
            messages.success(request, "Property Updated." )
            form.save()
            return redirect("view_property")
        return redirect("edit_property")
    
    

        
        
        
        
        
        
        
        
        
        
        
        

