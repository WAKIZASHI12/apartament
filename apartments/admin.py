from django.contrib import admin

from .models import Apartament, ApartmentImage, Booking, User, Review

class ApartamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'price', 'num_rooms', 'is_available', 'latitude', 'longitude']
    search_fields = ['name', 'address']

class ApartmentImageAdmin(admin.ModelAdmin):
    list_display = ['apartment', 'image']

class BookingAdmin(admin.ModelAdmin):
    list_display = ['apartment', 'start_date', 'end_date', 'is_booked']
    list_filter = ['start_date', 'end_date']

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    search_fields = ['username', 'email']

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['apartment', 'user', 'rating', 'comment']
    list_filter = ['rating']

admin.site.register(Apartament, ApartamentAdmin)
admin.site.register(ApartmentImage, ApartmentImageAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)