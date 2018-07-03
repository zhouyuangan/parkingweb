from django.contrib import admin
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('pk','user_name','car_number','car_type','car_color','car_kind')
    # exclude = ('user_name','car_number',)

