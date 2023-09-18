from django import forms  

# importamos los modelos
from .models import PetOwner, Pet


#
#
class OwnerForm(forms.ModelForm):
    
     #
     #
     
    class Meta:
        model = PetOwner  # 1
        fields = "first_name", "last_name", "address", "email", "phone" #2
        
            
        