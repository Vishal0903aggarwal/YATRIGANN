from django.shortcuts import render
from bookings.models import Destination, Category

def home(request):
    # Fetch only destinations marked as 'is_trending'
    trending_places = Destination.objects.filter(is_trending=True)
    # Fetch all categories for the navigation/icons
    categories = Category.objects.all()
    
    context = {
        'trending_places': trending_places,
        'categories': categories,
    }
    return render(request, 'index.html', context)