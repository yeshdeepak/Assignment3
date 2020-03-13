
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
   add_form = CustomUserCreationForm
   form = CustomUserChangeForm
   model = CustomUser
   list_display = ['username','first_name','last_name','email','Street_Address','City','State','Zip','Phone','User_Role']
   fieldsets = UserAdmin.fieldsets + (
      ('Additional info', {'fields': ('Street_Address','City','State','Zip','Phone','User_Role',)}),
   )


admin.site.register(CustomUser,CustomUserAdmin)
from django.contrib import admin

# Register your models here.
