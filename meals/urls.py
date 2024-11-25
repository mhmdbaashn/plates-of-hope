from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_restaurant, name='register_restaurant'),
    path('dashboard/', views.restaurant_dashboard, name='restaurant_dashboard'),
    path('add_meal/', views.add_meal, name='add_meal'),
    path('update_meal/<int:meal_id>/', views.update_meal, name='update_meal'),
    path('delete_meal/<int:meal_id>/', views.delete_meal, name='delete_meal'),
]