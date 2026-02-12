from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import TravelService, Booking, Destination
from .forms import BookingForm, TravelServiceForm

# Create your views here.
def search_results(request):
    query = request.GET.get('q') # Get the text from the search bar
    category_id = request.GET.get('category') # Get selected category ID
    
    results = TravelService.objects.all()

    if query:
        results = results.filter(destination__city__icontains=query)
    
    if category_id:
        results = results.filter(category_id=category_id)

    return render(request, 'bookings/search_results.html', {
        'results': results,
        'query': query
    })
    
def service_detail(request, pk):
    service = get_object_or_404(TravelService, pk=pk)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Create booking object but don't save to DB yet
            booking = form.save(commit=False)
            booking.user = request.user
            booking.service = service
            booking.total_amount = service.price
            booking.status = 'Confirmed'
            booking.save()
            return render(request, 'bookings/success.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'bookings/service_detail.html', {
        'service': service,
        'form': form
    })

# Only allow superusers to access this
@user_passes_test(lambda u: u.is_superuser)
def admin_dashboard(request):
    services = TravelService.objects.all()
    destinations = Destination.objects.all()
    return render(request, 'bookings/admin_dashboard.html', {
        'services': services,
        'destinations': destinations
    })

@user_passes_test(lambda u: u.is_superuser)
def delete_service(request, service_id):
    service = get_object_or_404(TravelService, id=service_id)
    service.delete()
    return redirect('admin_dashboard')

@user_passes_test(lambda u: u.is_superuser)
def add_service(request):
    if request.method == 'POST':
        form = TravelServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TravelServiceForm()
    return render(request, 'bookings/add_service.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def edit_service(request, service_id):
    service = get_object_or_404(TravelService, id=service_id)
    if request.method == 'POST':
        form = TravelServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = TravelServiceForm(instance=service)
    return render(request, 'bookings/edit_service.html', {'form': form, 'service': service})