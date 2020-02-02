from menu.models import Menu,Restaurant
from rest_framework import serializers


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        #fields = ('name', 'restaurant_location', 'date', 'time', 'price')
        fields = ('en_name', 'kr_name', 'price', 'restaurant', 'type')
        #fields = '__all__'


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'code', 'en_name', 'kr_name', 'operating_hours', 'hours_breakfast','hours_lunch', 'hours_dinner', 'location', 'latitude', 'longitude')
        #fields = '__all__'

