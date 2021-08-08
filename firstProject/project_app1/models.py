from django.db import models

# Create your models here.

class RegisteredUser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phoneNum = models.CharField(brank=True, null=True, max_length=20)