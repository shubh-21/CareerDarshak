from django.db import models

# Create your models here.
class Contact(models.Model):
    Gender = models.CharField(max_length=1,default='')
    SSC = models.CharField(max_length=3,default='')
    HSC = models.CharField(max_length=3,default='')
    Phy = models.CharField(max_length=3,default='')
    Chem = models.CharField(max_length=3,default='')
    Bio = models.CharField(max_length=3,default='')
    Maths = models.CharField(max_length=3,default='')
    NatureWork = models.CharField(max_length=2,default='')
    Literacy = models.CharField(max_length=1,default='')
    Living = models.CharField(max_length=1,default='')
    Finance = models.CharField(max_length=1,default='')
    hrs = models.CharField(max_length=2,default='')
    CreativeThink = models.CharField(max_length=2,default='')
    SelfLearn = models.CharField(max_length=2,default='')
    Coding =models.CharField(max_length=2,default='')
    Pubskill = models.CharField(max_length=2,default='')
    Comp = models.CharField(max_length=1,default='')
    Extracurr = models.CharField(max_length=1,default='')
    Teams = models.CharField(max_length=1,default='')
    Sports = models.CharField(max_length=1,default='')
    ReadWrite =models.CharField(max_length=3,default='')
    Subject = models.CharField(max_length=3,default='')
    HWSW = models.CharField(max_length=1,default='')
    gap = models.CharField(max_length=1,default='')
    


class User(models.Model):
    name=models.CharField(max_length=30,default="")
    email=models.CharField(max_length=30,default="")
    phoneno=models.CharField(max_length=11,default="")

    def __str__(self) -> str:
        return self.name

class Feedback(models.Model):
    name=models.CharField(max_length=30,default="")
    email=models.CharField(max_length=30,default="")
    message=models.CharField(max_length=50,default="")

    def __str__(self) -> str:
        return self.name

