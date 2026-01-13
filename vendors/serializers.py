from rest_framework import serializers
from .models import Vendor

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "owner", "business_name", "address"]
        extra_kwargs = {
            "owner" : {"read_only" : True}
        }