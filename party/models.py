import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from core import settings


class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="organized_parties")

    class Meta:
        verbose_name_plural = "parties"

    def __str__(self):
        return f"{self.venue}, {self.party_date}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    gift = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True, max_length=200)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="gifts")


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")

    def __str__(self):
        return f"{self.name}"
