from unicodedata import name
from django.db import models

from Authentication.models import RepeatFields

""" 
"""
    
class Site_Informations(RepeatFields): 
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    copyright = models.TextField()
    logo = models.ImageField(upload_to="Logo__Image")
    
 
class About_us_section(RepeatFields): 
    main_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField()
    
    

class Contact(RepeatFields):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    

    
