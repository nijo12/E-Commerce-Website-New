from django.db import models

class customerdb(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm_Password = models.CharField(max_length=100, null=True, blank=True)
