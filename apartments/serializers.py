from dataclasses import field
from rest_framework import serializers
from .models import Apartament, Booking


class ApartamentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apartament
        fields = ['id', 'name', 'address', 'price', 'num_rooms', 'is_available', 'latitude', 'longitude']
        class Meta:
            model = Apartament
            fields = ['id', 'owner', 'title', 'description', 'latitude', 'longitude', 'created_at']
            read_only_fields = ['owner', 'created_at']

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'apartment', ' start_date', ' end_date', 'is_booked']
        from rest_framework import serializers

