"""from django.urls import path
from django.contrib.auth import views as auth_views # Import Django's auth views
from . import views

urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-payments/', views.my_payments, name='my_payments'),
    path('signup/', views.signup_view, name='signup'),
    
    # New Login Path
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # 
    
    # New Logout Path
    path('logout/', views.logout_view, name='logout'),
]"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    
    # Add these two lines specifically:
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('my-payments/', views.my_payments, name='my_payments'),
]