from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=35, null=True, blank=True)
    age = models.DecimalField(max_digits=3, decimal_places=3, null=True, blank=True)
    skin_tone = models.CharField(max_length=35, null=True, blank=True)
    body_shape = models.CharField(max_length=35, null=True, blank=True)
    mobile_number = models.CharField(max_length=12, null=True, blank=True)
    avatar = models.FileField(upload_to='../media/avatars/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to='../media/images/', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email
