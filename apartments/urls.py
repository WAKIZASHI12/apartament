from django.urls import path
from. import views

urlpatterns = [
    path('apartments/', views.ApartmentListView.as_view(), name='apartment_list'),
    path('apartments/<int:pk>/', views.ApartmentDetailView.as_view(), name='apartment_detail'),
    path('bookings/', views.BookingView.as_view(), name='booking'),
    
]
