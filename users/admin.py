from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Professor, Aluno

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Aluno)
admin.site.register(Professor)
