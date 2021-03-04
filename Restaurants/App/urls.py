from django.urls import path,include
from App import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('Restaurants',views.RestaurantsAPIView)
router.register('Booking',views.BookingAPIView)
router.register('rating',views.RatingAPIView)
urlpatterns = [
    path('',include(router.urls)),
   # path('test',views.mobi)
]
