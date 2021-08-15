from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from cars.views import (create_add, home_page, car_detail,
                        user_car, car_update, car_delete, search)

urlpatterns = [
    path('car-update/<int:pk>/', car_update, name='car_update'),
    path('car-delete/<int:pk>/', car_delete, name='car_delete'),
    path('car-detail/<int:pk>/', car_detail, name='car_detail'),
    path('user-car/', user_car, name='user_car'),
    path('search/', search, name='search'),
    path('car-add/', create_add, name='car-add'),
    path('', home_page, name='home_page'),
]