from django.db import models
# from django.contrib.auth.models import User

# class Meal(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     quantity = models.PositiveIntegerField()
#     expiry_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     restaurant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meals')
#     is_available = models.BooleanField(default=True)
#     location = models.CharField(max_length=255)