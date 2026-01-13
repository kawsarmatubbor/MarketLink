from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "order_id", "customer", "vendor", "variant", "status", "total_amount"]
        extra_kwargs = {
            "customer": {"read_only": True},
            "vendor": {"read_only": True},
            "status": {"read_only": True},
            "total_amount": {"read_only": True}
        }

    def create(self, validated_data):
        customer = validated_data["customer"]
        variant = validated_data["variant"]

        order = Order.objects.create(
            customer=customer,
            vendor=variant.service.vendor,
            variant=variant,
            status="pending",
            total_amount=variant.price
        )

        return order
