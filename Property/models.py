from django.db import models
from django.contrib.auth import get_user_model

from Authentication.models import RepeatFields 

class InactiveProperties(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inactive = models.BooleanField(default=False)
    

class AdditionalPropertyImage(RepeatFields):
    image1 = models.ImageField(upload_to="Additional_Images")
    image2 = models.ImageField(upload_to="Additional_Images")
    image3 = models.ImageField(upload_to="Additional_Images")
    image4 = models.ImageField(upload_to="Additional_Images")
    image5 = models.ImageField(upload_to="Additional_Images")
    
    def __str__(self):
        return self.image1


class Bedrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class Bathrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class Garages(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class TypeProperty(RepeatFields):    
    property_type = models.CharField(max_length=254)
    
    def __str__(self):
        return self.property_type

class Properties(InactiveProperties):
    FOR_SALE = "FOR SALE"
    FOR_RENT = "FOR RENT"
    
    TYPE = [
        (FOR_SALE , "For Sale"),
        (FOR_RENT , "For Rent")
    ]
    
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    status  = models.CharField(choices=TYPE , max_length=150)
    bedroom = models.ForeignKey(Bedrooms, on_delete=models.SET_NULL , null=True , related_name="properties_bedrooms")
    bathroom = models.ForeignKey(Bathrooms, on_delete=models.SET_NULL , null=True , related_name="properties_bathrooms")
    garage = models.ForeignKey(Garages, on_delete=models.SET_NULL , null=True , related_name="properties_garages")
    address_name = models.CharField(max_length=254)
    property_type = models.ForeignKey(TypeProperty , on_delete=models.SET_NULL , null=True , related_name = "type_property")
    description = models.TextField()
    main_image = models.ImageField(upload_to='Property_images')
    users = models.ForeignKey(get_user_model() , on_delete=models.SET_NULL , null=True , related_name='property_user_id')
    
    def __str__(self):
        return self.name

    
    
    
    
    
    
    
    
