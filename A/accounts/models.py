from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'        # bar asas in fild etebar sanji mishe --> har chizi ke inja bashe bayad
    # unique=True
    REQUIRED_FIELDS = ['email']            #vaghti create super user mizanim che fild hayi ro begire

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):         #staff be karbar hayi gofte mishe k ejaze daran vared admin panel beshan
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin