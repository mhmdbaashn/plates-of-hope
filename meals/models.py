from django.db import models
from django.contrib.auth.models import User

# Restaurant model
class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Meal model
class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    expiry_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('claimed', 'Claimed')], default='available')

    def __str__(self):
        return self.name