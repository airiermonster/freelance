from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom User model for the Freelance Platform.
    Extends Django's AbstractUser to add additional fields.
    """
    ROLE_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('CLIENT', 'Client'),
        ('FREELANCER', 'Freelancer'),
    )

    role = models.CharField(
        verbose_name='User Role',
        max_length=10,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )
    bio = models.TextField(
        verbose_name='Biography',
        blank=True
    )
    profile_picture = models.ImageField(
        verbose_name='Profile Picture',
        upload_to='profile_pictures/',
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        verbose_name='Phone Number',
        max_length=15,
        blank=True
    )
    address = models.CharField(
        verbose_name='Address',
        max_length=255,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
