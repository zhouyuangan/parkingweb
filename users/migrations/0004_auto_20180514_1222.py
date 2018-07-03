# Generated by Django 2.0.5 on 2018-05-14 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180510_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(default='', max_length=15, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='car_color',
            field=models.CharField(default='', max_length=8, verbose_name='车色'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='car_kind',
            field=models.CharField(default='', max_length=8, verbose_name='车种'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='car_number',
            field=models.CharField(default='', max_length=11, verbose_name='车牌号'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='car_type',
            field=models.CharField(default='', max_length=11, verbose_name='车型'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_phone',
            field=models.CharField(default='', max_length=15, verbose_name='手机号码'),
        ),
    ]