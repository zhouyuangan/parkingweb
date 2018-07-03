from django.contrib import admin
from .models import Tariffs,Tickets
# Register your models here.
@admin.register(Tickets)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk','ticket_type','per_hour_money')

@admin.register(Tariffs)
class TariffsAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','car_number','start_time','ticket_type','parking_time','parking_money')
    exclude = ('per_hour_money',)
