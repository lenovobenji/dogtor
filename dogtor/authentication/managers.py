from django.contrib.auth.models import BaseUserManager


class ModUserManager (BaseUserManager):
    """Mod User Custom Manager"""
    
    
    
    #1. Creater_user
    #benji --->
    def create_user(self, email, user_name, first_name, password, **other_fields):
        """Overriding creater_user func for ModUserManager."""
        
        # Agregarr Validacion 
        
        if not email:
            raise ValueError("You must provide an email")
        
        email = self.normalize_email(email)
        # Nos hiso el usuario en la variable user
        user = self.model(email= email, user_name=user_name, first_name=first_name,**other_fields)
        
        # Seteamo password
        user.set_password(password)
        
        # Guardar en la base de datos 
        
        user.save()
        return user
        
    def create_superuser(self, email, user_name, first_name, password, **other_fields): 
           """Overriding creater_superuswr func for ModUserManager."""
           
           
        #is_staff --> Verdadero
        #is_activate 
        #is_superuser-->Verdadero
        
           other_fields.setdefault("is_staff", True)
           other_fields.setdefault("is_active", True)
           other_fields.setdefault("is_superuser", True)
            
            # Creamos el superior con la recoen creada 
           return self.create_user(email, user_name, first_name, password, **other_fields)
                                
           
           
           
        
    # 2. create_superuser
    # admin --> iifjfi -->creatersuperuser