from django.urls import path
from .views import OrderViewSet, payment_success, payment_fail, payment_cancel

urlpatterns = [
    path('orders/', OrderViewSet.as_view(), name='orders'),
    path('payment/success/<str:order_id>/', payment_success, name='payment_success'),
    path('payment/fail/<str:order_id>/', payment_fail, name='payment_fail'),
    path('payment/cancel/<str:order_id>/', payment_cancel, name='payment_cancel'),
]
