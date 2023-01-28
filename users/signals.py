from django.db.models.signals import post_save
from .views import addNotification
from .models import GuideInfo

def addGuide(sender,instance,created,**kwargs):

    if created:
     addNotification(instance)





post_save.connect(addGuide,sender=GuideInfo)   