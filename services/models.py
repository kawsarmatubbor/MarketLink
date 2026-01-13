from django.db import models

# Services model
class Service(models.Model):
    vendor = models.ForeignKey("vendors.Vendor", on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    description = models.TextField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name

# Service variant model
class ServiceVariant(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_minutes = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service.service_name}({self.variant_name})"