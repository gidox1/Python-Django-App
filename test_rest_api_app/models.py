from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings ##imports the settings.py file


class UserProfileManager(BaseUserManager):
    """Manager for the user profile"""

    def create_user(self, email, name, password = None):
        """Creates a new user profile"""
        if not email:
            raise ValueError('user must have email')

        email = self.normalize_email(email) 
        user = self.model(email=email, name=name) 
        user.set_password(password) 
        user.save(using=self._db) 

        return user
    
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with the given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system""" 
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False) 

    objects = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] 

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """Return string representation of the model"""
        return self.email 


class ProfileFeedItem(models.Model):
    """Profile status Update"""

    user_profile = models.ForeignKey(
     settings.AUTH_USER_MODEL, ##Targets the UserProfile model  
     on_delete=models.CASCADE, ##Cascade the changes down to the asssociated fields in the foriegn table  
    )

    status_text=models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return model as a string"""

        return self.status_text