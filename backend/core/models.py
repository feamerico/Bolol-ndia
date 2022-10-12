from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Cupcake(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)  # type: ignore
    inventory = models.IntegerField()

    def __str__(self):
        return self.title
