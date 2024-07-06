from django.db import models
from django import forms
from django.core.exceptions import ValidationError

def validate_judul(value):
    judul = value
    if judul == "einstein":
        msg = "maaf einstein tidak boleh disini!"
        raise ValidationError(msg)

# Create your models here.
class PostModel(models.Model):
    judul = models.CharField(max_length=20,validators=[validate_judul])
    body = models.TextField()
    category = models.CharField(max_length=20)
    
    def __str__(self) :
        return "{}. {}".format(self.id,self.judul)
    


    