import os
import uuid

from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


def get_file_path_profile_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('profile', filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)
    phone_number = PhoneNumberField(unique=True)
    image = models.ImageField(upload_to=get_file_path_profile_image,
                              null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    doctors = models.ManyToManyField("Doctor", related_name='customers', blank=True, null=True)
    weight = models.PositiveSmallIntegerField(null=True, blank=True)
    height = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'


class Doctor(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='doctor',
                                on_delete=models.CASCADE)
    field = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    experience = models.PositiveSmallIntegerField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'Doctor {self.user.username}'
