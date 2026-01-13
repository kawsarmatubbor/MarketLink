from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .sslcom import create_sslcommerz_session
from rest_framework.decorators import api_view

class OrderViewSet(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(customer = request.user)
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            order = serializer.save(
                customer = request.user
            )

            variant = serializer.validated_data["variant"]
            if variant.stock < 1:
                return Response({
                    "error": "This service variant is unavailable."
                })

            variant.stock -= 1
            variant.save()

            payment = create_sslcommerz_session(order)

            return Response({
                "success" : "Order place successful.",
                "payment_url" : payment["GatewayPageURL"],
                "order" : serializer.data
            })
        return Response(serializer.errors)

@api_view(['POST'])
def payment_success(request, order_id):
    try:
        order = Order.objects.get(order_id = order_id)
        order.status = "paid"
        order.save()
        return Response({
            "success" : "Payment success."
        })
    except Order.DoesNotExist:
        return Response({
            "error" : "Payment fail."
        })

@api_view(['POST'])
def payment_fail(request, order_id):
    return Response({
        "success" : "Payment fail."
    })

@api_view(['POST'])
def payment_cancel(request, order_id):
    return Response({
        "success" : "Payment cancel."
    })