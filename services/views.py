from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, ServiceVariant
from .serializers import ServiceSerializer, ServiceVariantSerializer
from .permissions import IsVendorOrAdminOrReadOnly
from vendors.models import Vendor

class ServiceViewSet(APIView):
    permission_classes = [IsVendorOrAdminOrReadOnly]

    def get(self, request):
        services = Service.objects.filter(is_active = True)
        serializer = ServiceSerializer(services, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ServiceSerializer(data = request.data)
        
        try:
            vendor = Vendor.objects.get(owner=request.user)
        except Vendor.DoesNotExist:
            return Response({
                "error" : "You are not a vendor."
            })

        if serializer.is_valid():
            serializer.save(
                vendor = vendor
            )
            return Response({
                "success" : "Service create successful.",
                "service" : serializer.data
            })
        return Response(serializer.errors)
    
class ServiceVariantViewSet(APIView):
    permission_classes = [IsVendorOrAdminOrReadOnly]

    def get(self, request, id):
        try:
            service = Service.objects.get(id = id)
        except Service.DoesNotExist:
            return Response({
                "error" : "Service not found."
            })
        
        service_variants = ServiceVariant.objects.filter(service = service)
        serializer = ServiceVariantSerializer(service_variants, many = True)
        return Response(serializer.data)
    
    def post(self, request, id):
        try:
            vendor = Vendor.objects.get(owner = request.user)
        except Vendor.DoesNotExist:
            return Response({
                "error" : "Your not a vendor."
            })
        
        try:
            service = Service.objects.get(id = id)
        except Service.DoesNotExist:
            return Response({
                "error" : "Service not found."
            })
        
        if service.vendor != vendor:
            return Response({
                "error" : "You can't create variants for this service."
            })
        
        serializer = ServiceVariantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(
                service = service
            )
            return Response({
                "success" : "Service variant create successful.",
                "service_variant" : serializer.data
            })
        return Response(serializer.errors)