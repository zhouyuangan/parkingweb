from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import CarPosition
from tariff.models import Tariffs,Tickets
from users.models import UserInfo
from django.utils import timezone
import time
import random

# Create your views here.

def car_posi_index(request):
    positions_list = CarPosition.objects.filter(position_status=True)
    context = {}
    context['positions_list'] = positions_list    
    return render(request,'car_posi_index.html',context)

def order_position(request,posi_pk):
    order_info = get_object_or_404(CarPosition,pk=posi_pk)
    # 更改车位库存信息
    car_order = CarPosition()
    car_order.pk = posi_pk
    car_order.position_num = order_info.position_num
    car_order.position_status = False
    car_order.save()

    # 增加票务信息
    user_info = UserInfo.objects.get(user_name=request.user.username) #获取用户信息
    ticket = Tickets.objects.order_by('-per_hour_money')
    tariff = Tariffs()
    tariff.user_name = request.user.username
    tariff.car_number = user_info.car_number
    tariff.ticket_type = 'Hour'
    pt = random.choice((0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5))
    tariff.parking_time = pt #
    tariff.parking_money = pt * ticket[0].per_hour_money
    tariff.save()    
    return HttpResponse('尊敬的{0}已预约了{1}'.format(request.user.username,order_info.position_num))

