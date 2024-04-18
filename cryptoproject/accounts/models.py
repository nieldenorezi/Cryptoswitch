from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    phone_number = models.IntegerField()
    # refferal_id = 
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"