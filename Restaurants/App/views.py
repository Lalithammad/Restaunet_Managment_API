from django.shortcuts import render
from .models import RestaurantsModel, BookingModel,RatingModel
from App.serializers import RestaurantsSerializers,BookingSerializers,RatingSerializers
from rest_framework  import viewsets
from rest_framework import serializers
from rest_framework.response import Response


# Create your views here.
class RestaurantsAPIView(viewsets.ModelViewSet):
    queryset = RestaurantsModel.objects.all()
    serializer_class = RestaurantsSerializers
    #def create(self, request, *args, **kwargs):

        # serializer = serializers.RatingSerializers(data = request.data, many=True)
        # rest_serializer = serializers.RestaurantsSerializers(data = request.data)
        # serializer = self.get_serializer(serializer=request.data)
        # serializer.is_valid(raise_exception=True)
        # data = serializer.objects.getlist('rating')
        # self.perform_create(data = data, Restaurants = RestaurantsModel.objects.last())#last recent data check
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
class BookingAPIView(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializers
class RatingAPIView(viewsets.ModelViewSet):
    queryset = RatingModel.objects.all()
    serializer_class = RatingSerializers
#conditons check for database data.
# def mobi(request):
#     if request.method == "POST":
#         number = request.POST.get('number')
#         alternate = request.POST.get('alternate')
#         if number == alternate:
#             print("Same number")
#         if number:#filter used for check condition in database.
# exists used for this filter condition exist or not in database.
#             if test.objects.filter(mobile = number).exists() or test.objects.filter(mobile = alternate).exists():
#                 print("Already registered")
#             if test.objects.filter(alternate = number).exists() or test.objects.filter(alternate = alternate).exists():
#                 print("Already Registered")

#         if alternate:
#             if test.objects.filter(mobile = number).exists() or test.objects.filter(mobile = alternate).exists():
#                 print("Already registered")

#             if test.objects.filter(alternate = number).exists() or test.objects.filter(alternate = alternate).exists():
#                 print("Already Registered")
#         # data = test(alternate=alternate,mobile=number)
#         # data.save()
#         return render(request,"test.html")

#     else:
#         a = test.objects.all()
#         print(a)
#         for x in a:
#             print(x.mobile,x.alternate)
#         return render(request,"test.html")