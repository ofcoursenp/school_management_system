from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    created_on = models.DateTimeField(auto_now_add=True)
    auth_token = models.CharField(max_length=24)
    is_verified = models.BooleanField(default=False)
    bio = models.CharField(max_length=300)
    profilePic = models.ImageField(null=True,blank=True,upload_to='images/profile/')
