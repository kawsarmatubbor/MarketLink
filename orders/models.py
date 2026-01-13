from django.db import models
import uuid

# Order model
class Order(models.Model):
    STATUS_CHOICE = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
        ("cancelled", "Cancelled"),
    ]

    order_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    customer = models.ForeignKey("accounts.CustomUser", on_delete=models.CASCADE)
    vendor = models.ForeignKey("vendors.Vendor", on_delete=models.CASCADE)
    variant = models.ForeignKey("services.ServiceVariant", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICE, default="pending", max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_id