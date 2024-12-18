from django.shortcuts import render
from vendor.models import *

def home(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    context = {
        'vendors': vendors,
    }
    print(vendors)
    return render(request, 'home.html', context)
