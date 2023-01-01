from django.db import models
import uuid
from json import dumps

# Create your models here.

class Packages(models.Model):
    packageName= models.CharField(max_length=100)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    description= models.TextField(max_length=2000,null=True,blank=True)
    packageDuration= models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=True, blank = True)
    vote_total= models.IntegerField(default=0, null=True,blank=True)
    ratings= models.IntegerField(default=0, null=True,blank=True)
    featured_img = models.ImageField(null=True,blank=True,default='default.jpg')
    itenary=models.JSONField(default={'itenary':[]})
    isUnderRated= models.BooleanField(default=False)

    
    def __str__(self):
       return self.packageName

   
