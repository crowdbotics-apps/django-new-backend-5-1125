from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    dada = models.BigIntegerField(null=True, blank=True,)
    r1 = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="customtext_r1",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
