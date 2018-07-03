from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(u'用户名',max_length=15,default='')    
    user_phone = models.CharField(u'手机号码',max_length=15,default='')
    car_number = models.CharField(u'车牌号',max_length=11,default='')
    car_type = models.CharField(u'车型',max_length=11,default='')
    car_color = models.CharField(u'车色',max_length=8,default='')
    car_kind = models.CharField(u'车种',max_length=8,default='')
    # balance = models.FloatField(u'余额')

    def __str__(self):
        return u'%s' % self.car_number

    class Meta:        
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
    
