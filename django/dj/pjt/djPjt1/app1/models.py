from django.db import models 
# Create your models here.
class tbl_userInfo(models.Model):
    user_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    device_id = models.CharField(max_length=30)
   
    
class tbl_eduImage(models.Model):
    image_name = models.CharField(max_length=30, unique=True)
    image_path = models.CharField(max_length=50)

