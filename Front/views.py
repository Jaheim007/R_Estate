from django.shortcuts import render
from django.views.generic import View

class Home(View):
    template_name = 'page/index.html'
    
    def get(self , request):
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
        pass
    
class Service(View):
    template_name = 'page/services.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self, request):
        pass
    


