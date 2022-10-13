from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


from Authentication.models import RepeatFields 

class InactiveProperties(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inactive = models.BooleanField(default=False)
    

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
    
class Cities(RepeatFields):
    city = models.CharField(max_length=150)
    
    def __str__(self):
        return self.city

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
    bedroom = models.ForeignKey(Bedrooms, on_delete=models.SET_NULL ,blank=True , null=True , related_name="properties_bedrooms")
    bathroom = models.ForeignKey(Bathrooms, on_delete=models.SET_NULL ,blank=True , null=True , related_name="properties_bathrooms")
    garage = models.ForeignKey(Garages, on_delete=models.SET_NULL ,blank=True ,  null=True , related_name="properties_garages")
    location = models.ForeignKey(Cities , on_delete=models.SET_NULL, null=True, related_name='location_cities')
    property_type = models.ForeignKey(TypeProperty , on_delete=models.SET_NULL ,blank=True ,  null=True , related_name = "type_property")
    description = RichTextField(blank=True , null=True)
    main_image = models.ImageField(upload_to='Property_images')
    additional_image1 = models.ImageField(upload_to="Additional_Images" , blank=True)
    additional_image2 = models.ImageField(upload_to="Additional_Images" , blank=True)
    additional_image3 = models.ImageField(upload_to="Additional_Images" , blank=True)
    users = models.ForeignKey(get_user_model() , on_delete=models.SET_NULL , null=True , related_name='property_user_id')

    
    def __str__(self):
        return self.name


class RequestTime(RepeatFields):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    save_user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True ,  related_name='user_request')

    
    def __str__(self):
        return self.name
    
    
    
    
    
