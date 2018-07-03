from django.db import models
from users.models import UserInfo
# Create your models here.

class Tariffs(models.Model):
    # user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    user_name = models.CharField(u'用户',default='abc',max_length = 20)
    car_number = models.CharField(u'车牌号',max_length=20)
    start_time = models.DateTimeField(u'开始时间',auto_now_add=True)
    end_time = models.DateTimeField(u'结束时间',auto_now=True)
    parking_time = models.FloatField(verbose_name='停车时间(小时)',default=0.0,editable=False,unique=False)
    parking_money = models.FloatField(verbose_name=u'停车费(元)',default=0.0,editable=False)
    TICKET_TYPE_CHOICES=(
        ('Hour',u'小时票'),
    )
    ticket_type = models.CharField(u'计费类型',
                                    max_length=20,
                                    choices=TICKET_TYPE_CHOICES)
    per_hour_money = models.FloatField(verbose_name=u'小时停车费',default=0.0,editable=True)
    def __str__(self):
        return u'%s' % self.ticket_type
    
    class Meta:
        verbose_name = '票务中心'
        verbose_name_plural = '票务中心'

class Tickets(models.Model):
    TICKET_TYPE_CHOICES=(
        ('Hour',u'小时票'),
    )
    ticket_type = models.CharField(u'计费类型',
                                    max_length=20,
                                    choices=TICKET_TYPE_CHOICES)
    per_hour_money = models.FloatField(verbose_name=u'小时停车费(元)',default=0.0,editable=True)
    
    class Meta:
        verbose_name = '收费类型'
        verbose_name_plural = '收费类型'