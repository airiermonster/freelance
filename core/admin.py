from django.contrib import admin
from .models import Category, Service, Project

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for Category model
    """
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Admin interface for Service model
    """
    list_display = ('title', 'provider', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'description', 'provider__username', 'provider__email')
    raw_id_fields = ('provider', 'category')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Admin interface for Project model
    """
    list_display = ('title', 'client', 'freelancer', 'budget', 'status', 'deadline', 'created_at')
    list_filter = ('status', 'category', 'created_at', 'deadline')
    search_fields = ('title', 'description', 'client__username', 'freelancer__username')
    raw_id_fields = ('client', 'freelancer', 'category')
