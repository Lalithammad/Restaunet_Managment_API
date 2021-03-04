from .models import RestaurantsModel,BookingModel,RatingModel
from rest_framework import serializers
from datetime import datetime
class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingModel
        fields = '__all__'

class RestaurantsSerializers(serializers.ModelSerializer):
    rating_serial = serializers.SerializerMethodField()
    class Meta:
        model = RestaurantsModel
        fields = '__all__'
    def get_rating_serial(self, obj):
        return RatingSerializers(RatingModel.objects.filter(Restaurants=obj),many = True).data
class BookingSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = BookingModel
        fields = '__all__'
    
    def validate(self,data):
        #print(data)
        selected_table = data['tableNumber']
        #print(selected_table)
        Restaurant=data['Restaurants']
        #print(Restaurant)
        slot=data['slots'] 
        #print(slot)
        bookingtime = data['Bookingdate']
        #print(bookingtime)
        Total_table= RestaurantsModel.objects.get(name=Restaurant)
        Total_table.total_tables #shows table data.
        #print(a)
        # today = datetime.now()
        # print(today)
        if(int(Total_table.total_tables) < int(selected_table)):
           raise serializers.ValidationError("Selected table out of range of total tables")
        
        if BookingModel.objects.filter(Restaurants = Restaurant).exists():
            if BookingModel.objects.filter(Bookingdate = bookingtime):    
                if BookingModel.objects.filter(slots = slot).exists():
                    if BookingModel.objects.filter(tableNumber = selected_table ).exists():
                        raise serializers.ValidationError("already booked!") 
        return data  
