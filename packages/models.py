from django.db import models
import uuid

# Create your models here.

class Package(models.Model):
    location = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    pkLength= models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid= models.UUIDField(default=uuid.uuid4,unique=True,editable=False, primary_key=True)
    price = models.IntegerField(null=True, blank = True)
    vote_total= models.IntegerField(default=0, null=True,blank=True)
    ratings= models.IntegerField(default=0, null=True,blank=True)
    featured_img = models.ImageField(null=True,blank=True,default='default.jpg')

    def __str__(self):
       return self.location

   
