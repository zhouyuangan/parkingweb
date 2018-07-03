from django.db import models

# Create your models here.

class CarPosition(models.Model):
    position_num = models.CharField('车位编号',max_length=20,default='')
    position_status = models.BooleanField('车位状态[默认为空闲]',default=True)
    class Meta:
        verbose_name = '车位'
        verbose_name_plural = '车位'