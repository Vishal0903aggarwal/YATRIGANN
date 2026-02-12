from logging import log
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from bookings.models import Booking

@login_required
def my_profile(request):
    return render(request, 'users/my_profile.html')

# 1. My Bookings Dashboard
@login_required 
def my_bookings(request):
    # Fetch bookings for the current user, ordered by the most recent booking
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    return render(request, 'users/my_bookings.html', {
        'bookings': user_bookings
    })

# 2. User Signup Logic
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after they sign up
            messages.success(request, "Registration successful! Welcome to YATRIGANN.", extra_tags='alert-success')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

# 3. Payment Logic
@login_required
def my_payments(request):
    # Fetch payments for the current user
    user_payments = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    return render(request, 'users/my_payments.html', {
        'payments': user_payments
    })
    
# 4. Logout Logic
def logout_view(request):
    logout(request)
    #messages.success(request, "You have been logged out successfully.")
    return redirect('home')