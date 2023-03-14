from django.db import models

class admindb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Mob_No = models.IntegerField(null=True,blank=True)
    User_Name = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)
    Image = models.ImageField(upload_to="Profile",null=True,blank=True)

class categorydb(models.Model):
    Category_Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=200,null=True,blank=True)
    Image = models.ImageField(upload_to="Profile",null=True,blank=True)

class productdb(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile", null=True, blank=True)

class contactdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=1000,null=True,blank=True)
