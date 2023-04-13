from rest_framework import serializers

from .models import City, PotentialCity


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)


class PotenCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialCity
        fields = ('name',)
