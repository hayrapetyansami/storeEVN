from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
    )
    country = models.CharField(blank=True, null=True, default=None)
    city = models.CharField(blank=True, null=True, default=None)
    address = models.CharField(blank=True, null=True, default=None)
    postal_code = models.CharField(blank=True, null=True, default=None)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
