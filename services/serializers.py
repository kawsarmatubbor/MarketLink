from rest_framework import serializers
from .models import Service, ServiceVariant

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'vendor', 'service_name', 'description']
        extra_kwargs = {
            "description" : {"required" : False},
            "vendor" : {"read_only" : True}
        }

class ServiceVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceVariant
        fields = ['id', 'service', 'variant_name', 'price', 'estimated_minutes', 'stock']
        extra_kwargs = {
            "service" : {"read_only" : True}
        }
