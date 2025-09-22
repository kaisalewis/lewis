from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("University info", {"fields": ("admission_number", "department", "school", "is_student")}),
    )
    list_display = ("username", "email", "admission_number", "department", "school", "is_staff", "is_active")

