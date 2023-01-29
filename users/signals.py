from django.db.models.signals import post_save
from .models import GuideInfo,guideNoti
from django.shortcuts import redirect


def addGuide(sender,instance,created,**kwargs):

    if created:
       print(instance)
       new_notification=guideNoti(guide=instance)
       new_notification.save()
       print("added")
       return redirect('home')




post_save.connect(addGuide,sender=GuideInfo)   