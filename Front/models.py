from django.db import models

from Authentication.models import RepeatFields

""" 
"""
class Banner(RepeatFields): 
    video = models.URLField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Newsletter_Section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Site_Informations(RepeatFields): 
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    copyright = models.TextField()
    logo = models.ImageField(upload_to="Logo__Image")
    
class Recent_Property_Section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Featured_Agents_Section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class About_us_section(RepeatFields): 
    main_title = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Teams_meet_section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Reviews_Section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Contact_section(RepeatFields): 
    title = models.CharField(max_length=150)
    description = models.TextField()
    
class Contact(RepeatFields):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()
    
class Newsletters(RepeatFields):
    email = models.EmailField()
    
