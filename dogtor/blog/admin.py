from django.contrib import admin

from. import models
# Register your models here.

# panel 
class BlogAdminArea(admin.AdminSite):
    
     site_header = "Blog Site Admin Area"
  
  # Instanciar nuestra clase para poder utilizar   
     
blog_admin_site = BlogAdminArea(name="BlogAdmin")



# Registre modelo 'Post' en nuestro admin area 
blog_admin_site.register(models.Post)  
admin.site.register(models.Post)   