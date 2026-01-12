from django.urls import path
from .views import VendorViewSet

urlpatterns = [
    path('vendors/', VendorViewSet.as_view(), name='vendors'),
]
