from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Restaurant, Meal

# Restaurant Registration Form
class RestaurantRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    address = forms.CharField(widget=forms.Textarea)
    contact = forms.CharField(max_length=15)

    class Meta:
        model = Restaurant
        fields = ('username', 'password1', 'password2', 'name', 'address', 'contact')

# Meal Form
class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('name', 'description', 'quantity', 'expiry_date')