from django.db import models
from datetime import datetime
# Create your models here.
class RatingModel(models.Model):
        rate = (
            (1,"1"),
            (2,"2"),
            (3,"3"),
            (4,"4"),
            (5,"5"),
        )
        username = models.CharField(max_length=20)
        rating = models.CharField(max_length=5,choices=rate,default=5)
        Restaurants = models.ForeignKey('RestaurantsModel',on_delete=models.CASCADE)
class RestaurantsModel(models.Model):
    categ = (
        ('Pure-Veg',"Pure-Veg"),
        ('Non-Veg',"Non-Veg"),
        ('Veg-NonVeg',"Veg-NonVeg")
    )
    name = models.CharField(max_length=100)
    image = models.ImageField()
    category = models.CharField(max_length=15,choices=categ,default="Pure-Veg")
    price = models.IntegerField()
    total_tables = models.CharField(max_length=5)    
    def __str__(self):
        return self.name
class BookingModel(models.Model):
    slot=(
        ('6PM to 7PM',"6PM to 7PM"),
        ('7PM to 8PM',"7PM to 8PM"),
        ('8PM to 9PM',"8PM to 9PM"),
        ('9PM to 10PM',"9PM to 10PM"),
        ('10PM to 11PM',"10PM to 11PM"),
        ('11PM to 12PM',"11PM to 12PM"),
        ('12PM to 1PM',"12PM to 1PM")   
    )
    Restaurants = models.ForeignKey(RestaurantsModel,on_delete=models.CASCADE)
    slots = models.CharField(max_length=12,choices=slot,default="10PM")
    tableNumber = models.CharField(max_length=5) 
    Bookingdate = models.DateField(default=datetime.now)

# class test(models.Model):
#     mobile = models.CharField(max_length=100, null=True, blank=True)
#     alternate = models.CharField(max_length=100, null=True, blank=True)
