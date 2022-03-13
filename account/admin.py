from django.contrib import admin

from .models import Profile, Doctor


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['phone_number',]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = ['field', 'gender',]