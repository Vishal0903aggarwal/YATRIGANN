from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    # e.g., Flight, Hotel, Bus, Holiday Package
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=50, help_text="FontAwesome icon class name")

    def __clstr__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    is_trending = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city}, {self.state}"

class TravelService(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # e.g. "IndiGo 6E-213" or "Taj Hotel Deluxe Room"
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=4.0)
    available_slots = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.category.name} - {self.title}"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(TravelService, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking #{self.id} by {self.user.username}"