from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
import uuid



class UserManager(BaseUserManager):
    def create_user(self, phone_number=None, email=None, password=None):
        if not phone_number and not email:
            raise ValueError("User must have either a phone number or email")
        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number=None, email=None, password=None):
        user = self.create_user(phone_number, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



