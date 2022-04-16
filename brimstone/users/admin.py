from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OldUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(OldUserAdmin):
    list_display = ('username', 'email', 'is_student')
    fieldsets = OldUserAdmin.fieldsets + (('User Type', {'fields': ('is_student',)}),)

