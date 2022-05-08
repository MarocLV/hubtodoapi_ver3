from django.contrib import admin
from .models import Tareas, Priority, Usuarios
#from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Tareas)

admin.site.register(Priority)

#admin.site.register(Usuarios, UserAdmin)