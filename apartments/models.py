from django.db import models

class Apartament(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    num_rooms = models.IntegerField()
    is_available = models.BooleanField(default=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='apartments/')

class Booking(models.Model):
    apartment = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_booked = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Review(models.Model):
    apartment = models.ForeignKey(Apartament, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    
    
