from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for User model
    """
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('role', 'bio', 'profile_picture', 'phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('role', 'bio', 'profile_picture', 'phone_number', 'address')}),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

# Register the User model with the custom admin interface
admin.site.register(User, CustomUserAdmin)
