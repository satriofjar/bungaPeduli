from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_file_size

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, null=True)

    avatar = models.ImageField(blank=True, null=True, validators=[validate_file_size])

    @property
    def imageURL(self):
        try :
            url = self.avatar.url
        except:
            url = ''
        return url


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    collected = models.BigIntegerField(null=True, blank=True)
    fund_target = models.BigIntegerField(null=True, blank=True)
    beneficiary = models.TextField(null=True)
    time_span = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    thumbnail = models.ImageField(blank=True, null=True, validators=[validate_file_size])

    
    @property
    def imageURL(self):
        try :
            url = self.thumbnail.url
        except:
            url = ''
        return url


class Donator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, null=True) 
    amount = models.BigIntegerField(null=True)
    comment = models.TextField(null=True, blank=True)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
