from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
provinces= [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
    ]
class GuideInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=200,blank=True,null=True)
    phone= models.IntegerField(unique=True)
    adresss1= models.CharField(max_length=200,blank=True,null=True)
    adresss2= models.CharField(max_length=200)
    province=models.IntegerField(choices=provinces,default='1')
    profileImage=models.ImageField(null=True,blank=True,default='userdp.png')
    cvFile= models.FileField(upload_to='cv/')
    fbLink= models.CharField(max_length=500,blank=True,null=True)
    instaLink= models.CharField(max_length=500,blank=True,null=True)
    shortIntro=models.TextField(max_length=500)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created=models.DateTimeField(auto_now_add=True)
    approvedByAdmin= models.BooleanField(default=False)
  
    def __str__(self):
       return self.name

class guideNoti(models.Model):
    guide= models.ForeignKey(GuideInfo,on_delete=models.RESTRICT)
    approved=models.BooleanField(default=False)  
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.guide.name
         



   
