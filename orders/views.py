from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order

class OrderViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(customer = request.user)
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(
                customer = request.user
            )

            variant = serializer.validated_data["variant"]
            if variant.stock < 1:
                return Response({
                    "error": "This service variant is unavailable."
                })

            variant.stock -= 1
            variant.save()

            return Response({
                "success" : "Order place successful.",
                "order" : serializer.data
            })
        return Response(serializer.errors)