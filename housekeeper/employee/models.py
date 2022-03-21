


from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import  RegexValidator

from generic.models import BaseField
from generic.models import BaseField



class role(models.Model):
    rolename = models.CharField(max_length=50)
    def __str__(self):
        return self.rolename
    
    class meta:
        db_table = "role"


class User(AbstractUser,BaseField):
    roleid = models.ForeignKey(role, on_delete=models.CASCADE )
    username = models.CharField(max_length = 99, unique = True)
  
    email = models.CharField(_('email address') ,max_length=150, unique=True)
  
    phone_number = models.CharField(max_length=10, blank=True, unique=True) 
    roleid = models.ForeignKey(role, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="user_img")
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    class Meta:
        db_table = "User"


    def __str__(self):
        return self.username

  