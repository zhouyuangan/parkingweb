from django.contrib import admin
from .models import CarPosition
# Register your models here.

@admin.register(CarPosition)
class CarPositionAdmin(admin.ModelAdmin):
    list_display = ('pk','position_num','position_status')