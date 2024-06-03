from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Apartament, Booking
from .serializers import ApartamentSerializers, BookingSerializers

class ApartmentListView(APIView):
    def get(self, request):
        apartments = Apartament.objects.all()
        serializer = ApartamentSerializers(apartments, many=True)
        return Response(serializer.data)

class ApartmentDetailView(APIView):
    def get(self, request, pk):
        apartment = Apartament.objects.get(pk=pk)
        serializer = ApartamentSerializers(apartment)
        return Response(serializer.data)

class BookingView(APIView):
    def post(self, request):
        serializer = BookingSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)