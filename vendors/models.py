from django.db import models

# Vendors model
class Vendor(models.Model):
    owner = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    address = models.TextField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name