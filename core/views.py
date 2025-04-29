from django.shortcuts import render
from .models import Category, Service, Project

def home(request):
    """
    Home page view
    """
    categories = Category.objects.all()[:5]
    services = Service.objects.filter(is_active=True)[:6]
    projects = Project.objects.filter(status='OPEN')[:6]

    context = {
        'categories': categories,
        'services': services,
        'projects': projects,
    }

    return render(request, 'core/home.html', context)
