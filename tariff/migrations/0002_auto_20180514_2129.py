# Generated by Django 2.0.5 on 2018-05-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tariffs',
            options={'verbose_name': '票务中心', 'verbose_name_plural': '票务中心'},
        ),
        migrations.RemoveField(
            model_name='tariffs',
            name='user',
        ),
        migrations.AddField(
            model_name='tariffs',
            name='parking_time',
            field=models.FloatField(default=0.0, editable=False, verbose_name='停车时间'),
        ),
        migrations.AddField(
            model_name='tariffs',
            name='user_name',
            field=models.CharField(default='abc', max_length=20, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='end_time',
            field=models.DateTimeField(auto_now=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='开始时间'),
        ),
        migrations.AlterField(
            model_name='tariffs',
            name='ticket_type',
            field=models.CharField(choices=[('Hour', '小时票')], max_length=20, verbose_name='计费类型'),
        ),
    ]
