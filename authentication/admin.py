from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import Usuarios

admin.site.register(Usuarios, UserAdmin)