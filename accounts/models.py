from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from operator import itemgetter
from django_extensions.db.models import (
    TimeStampedModel,
	ActivatorModel 
)


class UserProfile(TimeStampedModel,ActivatorModel,models.Model):
    class Meta:
        verbose_name_plural = 'User profiles'
        ordering = ["id"]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    telephone = models.CharField(verbose_name="Contact telephone number", max_length=255, null=True, blank=True)
    id = models.AutoField(primary_key=True)

    def full_name(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}'
        if self.user.email:
            return self.user.email
        return self.user.email

    def __str__(self):
        return self.full_name()

