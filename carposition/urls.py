from django.urls import path
from . import views

urlpatterns = [
    path('car_posi_index',views.car_posi_index,name='car_posi_index'),
    path('order_position/<int:posi_pk>',views.order_position,name='order_position'),
]