from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Vendor
from .serializers import VendorSerializer

class VendorViewSet(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        vendors = Vendor.objects.filter(is_active = True)
        serializer = VendorSerializer(vendors, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        if Vendor.objects.filter(owner = request.user).exists():
            return Response({
                "error" : "You already have a vendor profile."
            })
        
        serializer = VendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(
                owner = request.user
            )

            user = request.user
            if user.role == 'customer':
                user.role = 'vendor'
                user.save()

            return Response({
                "success" : "Vendor profile created.",
                "vendor" : serializer.data
            })
        return Response(serializer.errors)