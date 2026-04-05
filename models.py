from django.db import models
from django.utils import timezone

# Create your models here.


class FeedBack(models.Model):
    email=models.CharField(max_length=45,primary_key=True)
    name=models.CharField(max_length=55,null=False)
    rating=models.CharField(max_length=5,null=False)
    query=models.TextField(default="")
    user_pic=models.CharField(max_length=255,default="")
    date=models.DateField ( default=timezone.now)
    def __str__(self):### it represents object into string form ###     ###self means object#####
         return self.name

    

###### conatact table model####

class Contact (models.Model):
      email=models.CharField(max_length=45)
      name=models.CharField(max_length=55,null=False)  
      phone=models.CharField(max_length=13,null=False)
      question=models.TextField()
      date=models.DateField ( default=timezone.now)

      def __str__(self):### it represents object into string form ###     ###self means object#####
         return self.name


class User(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60,primary_key=True)
    password=models.CharField(max_length=45)
    phone=models.CharField(max_length=13)
    pic_name=models.FileField(upload_to="user_pic/",default="")   

class ShopOwner(models.Model):
     name=models.CharField(max_length=60)
     email=models.EmailField(max_length=60,primary_key=True)
     password=models.CharField(max_length=45)
     phone=models.CharField(max_length=13)
     pic_name=models.FileField(upload_to="owner_pic/",default="") 
     def __str__(self):### it represents object into string form ###     ###self means object#####
         return self.name
     

class ShopDetail(models.Model):
    owner=models.ForeignKey(ShopOwner,on_delete=models.DO_NOTHING)  ####foreign key is for one to manay a person can add many products 
    shop_name = models.CharField(max_length=255)
    gst_number= models.CharField(max_length=255,primary_key=True)
    description = models.TextField(blank=True, null=True)
    location_lat = models.CharField(max_length=100)
    location_long = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=15)  
    city=models.CharField(max_length=100)
    address = models.TextField(default="")     
        
    # owner,location lat ,location long fields are not to be included in shopdetail html page , enctype multitype........ to be included

status_type = [
    ('REQUESTED', 'Requested'),      
       
    ('RECEIVED', 'Medicine Received'), 
    ('CANCELLED', 'Request Cancelled'),
]

class MedicineRequest(models.Model):
    user_email=models.CharField(max_length=100,null=False)
    user_whatsapp=models.CharField(max_length=13,null=False)
    medicine_name=models.CharField(max_length=100,null=False)
    refer_doctor_name=models.CharField(max_length=100,null=True)
    user_message=models.TextField(default="",null=True)
    medicine_status=models.CharField(max_length=30,choices=status_type,default="REQUESTED")
    
