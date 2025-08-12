from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, ListingViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'listings', ListingViewSet, basename='listing')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
