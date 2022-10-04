from django.shortcuts import render
from django.views.generic import View

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
    
