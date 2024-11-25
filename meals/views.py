from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RestaurantRegistrationForm, MealForm
from .models import Meal, Restaurant
from django.contrib.auth.decorators import login_required

# Register a restaurant
def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Restaurant.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                contact=form.cleaned_data['contact']
            )
            login(request, user)
            return redirect('restaurant_dashboard')
    else:
        form = RestaurantRegistrationForm()
    return render(request, 'meals/register.html', {'form': form})

# Restaurant dashboard to list meals
@login_required
def restaurant_dashboard(request):
    meals = Meal.objects.filter(restaurant=request.user.restaurant)
    return render(request, 'meals/dashboard.html', {'meals': meals})

# Add a meal
@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.restaurant = request.user.restaurant
            meal.save()
            return redirect('restaurant_dashboard')
    else:
        form = MealForm()
    return render(request, 'meals/add_meal.html', {'form': form})

# Update a meal
@login_required
def update_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, restaurant=request.user.restaurant)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('restaurant_dashboard')
    else:
        form = MealForm(instance=meal)
    return render(request, 'meals/update_meal.html', {'form': form, 'meal': meal})

# Delete a meal
@login_required
def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, restaurant=request.user.restaurant)
    if request.method == 'POST':
        meal.delete()
        return redirect('restaurant_dashboard')
    return render(request, 'meals/delete_meal.html', {'meal': meal})