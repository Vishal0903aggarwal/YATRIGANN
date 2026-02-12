from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_results, name='search_results'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/delete/<int:service_id>/', views.delete_service, name='delete_service'),
    path('admin-panel/add/', views.add_service, name='add_service'),
]