from django.db import models
from django.core.validators import MinLengthValidator

class User(models.Model):
    username = models.CharField(max_length=100,validators=[MinLengthValidator(4)])
    password = models.CharField(max_length=16,validators=[MinLengthValidator(6)])
    telephone = models.CharField(max_length=11)

    # def __str__(self):
    #     return "app01 %s " % self.username

    class Meta:
        app_label = "front"

