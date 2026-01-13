from django.urls import path
from .views import ServiceViewSet, ServiceVariantViewSet

urlpatterns = [
    path('services/', ServiceViewSet.as_view(), name='services'),
    path('services/<int:id>/variants/', ServiceVariantViewSet.as_view(), name='services_variants'),
]
