from django.db import models
from django.conf import settings

class Category(models.Model):
    """
    Categories for freelance services
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Service(models.Model):
    """
    Services offered by freelancers
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='services')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

class Project(models.Model):
    """
    Projects created by clients
    """
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_projects')
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='freelancer_projects',
        null=True,
        blank=True
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
