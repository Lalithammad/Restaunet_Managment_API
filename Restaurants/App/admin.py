from django.contrib import admin
from App.models import RatingModel,RestaurantsModel,BookingModel
# Register your models here.
admin.site.register(RatingModel)
admin.site.register(RestaurantsModel)
admin.site.register(BookingModel)