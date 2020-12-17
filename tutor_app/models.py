from django.db import models
from django.utils import timezone

# Create your models here.
class stregister(models.Model):
    first=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    ph= models.IntegerField()
    gender=models.CharField(max_length=100)


class ttregister (models.Model):
        first = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        ph = models.IntegerField()
        gender = models.CharField(max_length=100)

class login (models.Model):
    status=models.IntegerField()
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class formtutor(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    dob=models.DateField()
    addr=models.TextField(max_length=300)
    pins=models.IntegerField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    exp=models.IntegerField()
    doj=models.DateField()
    online=models.CharField(max_length=100)
    hour=models.IntegerField()
    img=models.FileField()
    tutoring=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    fun=models.CharField(max_length=200)
    demo=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class booknow(models.Model):
    status = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    clas = models.CharField(max_length=100)
    board = models.CharField(max_length=100)
    cit = models.CharField(max_length=100)
    sid=models.IntegerField()
    tid=models.IntegerField()
    dof= models.DateField()
    day= models.IntegerField()
    hrb= models.IntegerField()







