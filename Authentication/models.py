from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField



class InactiveRepeatFields(models.Model):
    """
    This class was created in order to verify: 
    When was the user created.
    Updated for everytime a user wants to make updates to his user.  
    Inactive to verify if a user is still available or not.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inactive = models.BooleanField(default=False)
    

class RepeatFields(models.Model):
    """
    This class was created in order to verify: 
        When was the user created.
        Updated for everytime a user wants to make updates to his user.  
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class User(AbstractUser, InactiveRepeatFields):
    """
    This class contains all information such as:
        First name , Last Name , email , phone number , password , image , facebook id , instagram id , twitter id and linkedin id.
    """ 
    image = models.ImageField(upload_to='User__Images', blank=True)
    phone_number = PhoneNumberField(region='CI',  blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return self.username
    
    
    
