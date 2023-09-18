from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, PermissionsMixin 


from .managers import ModUserManager

# Manager 
class ModUser(AbstractUser, PermissionsMixin):
    
    """ Custom Moderator User """
    
    # sobrescribier propiedades
    
    
    
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=300, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    about = models.TextField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    
    # Manager del modeo
    objects = ModUserManager()
    
    #campo identificaoadr del user
    USERNAME_FIELD = "email"
    
    # Campos requeridos ´para cuando el comando createruser
    REQUIRED_FIELDS = ["user_name", "first_name"]
    
    # Metodos string
    def __str__(self):
        return f"{self.user_name} {self.email}"