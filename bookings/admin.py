from django.contrib import admin
from .models import Category, Destination, TravelService, Booking

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('city', 'state', 'is_trending')
    list_filter = ('state', 'is_trending')
    search_fields = ('city', 'name')

@admin.register(TravelService)
class TravelServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'destination', 'price', 'rating')
    list_filter = ('category', 'rating')
    search_fields = ('title', 'destination__city')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'travel_date', 'status', 'total_amount')
    list_filter = ('status', 'travel_date')
    readonly_fields = ('booking_date',) # Prevents changing the date the booking was made