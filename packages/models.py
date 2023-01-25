from django.db import models
import uuid
from json import dumps

# Create your models here.

class Packages(models.Model):
    packageName= models.CharField(max_length=100)
    location =models.CharField(max_length=100,null=True,blank=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    description= models.TextField(max_length=2000,null=True,blank=True)
    packageDuration= models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank = True)
    vote_total= models.IntegerField(default=0, null=True,blank=True)
    ratings= models.IntegerField(default=0, null=True,blank=True)
    itenary=models.TextField(max_length=1000,null=True,blank=True)
    isUnderRated= models.BooleanField(default=False)
    defimage= models.ImageField(null=True,blank=True,default='default.jpg')



    def __str__(self):
       return self.packageName


class Images(models.Model):
    packageName=models.ForeignKey(Packages,on_delete=models.CASCADE)
    image= models.ImageField(null=True,blank=True,default='default.jpg')
       
       
    def __str__(self):
       return self.image

   
