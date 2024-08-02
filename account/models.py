from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    picture = models.ImageField(upload_to="picture-profile/")