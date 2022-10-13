from django.shortcuts import render ,redirect
from django.views.generic import View
from django.contrib import messages #import messages
from django.http import JsonResponse
from django.db.models import Q

from Property import models
from Front import models as front

class Home(View):
    template_name = 'page/index.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass
    
class About(View):
    template_name = 'page/about.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass


class Contact(View):
    template_name = 'page/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        msg =''
        success = True
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            contact = front.Contact(
                name = name , 
                email = email, 
                subject = subject, 
                message=message
            )
        contact.save()
        msg = 'Thank you for contacting Medicio.'
            
        data = {
            'msg': msg,
            'success': success
        }

        return JsonResponse(data, safe=False)
    
class Service(View):
    template_name = 'page/services.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass
    


