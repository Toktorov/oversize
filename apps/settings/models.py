from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=250)
    decription = models.TextField()
    logo = models.ImageField(upload_to = 'logo/')
    tel = models.CharField(max_length=255)
    email = models.EmailField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class Action(models.Model):
    image = models.ImageField(upload_to = "action/")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"