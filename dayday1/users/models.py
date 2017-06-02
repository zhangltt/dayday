from django.db import models

# Create your models here.

class userLogin(models.Model):
    user_name = models.CharField(max_length=30)
    user_passwd = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'userLogin'

class userInfo(models.Model):
    phone = models.CharField(max_length=30,default='')
    address = models.CharField(max_length=100,default='')
    postcode = models.CharField(max_length=20,default='')
    recipient = models.CharField(max_length=20,default='')
    email = models.CharField(max_length=20,default='')
    user = models.ForeignKey('userLogin')
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'userInfo'
