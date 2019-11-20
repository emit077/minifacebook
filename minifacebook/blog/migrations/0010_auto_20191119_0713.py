# Generated by Django 2.2.7 on 2019-11-19 07:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20191116_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 7, 13, 15, 107727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 7, 13, 15, 106973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='accept_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 7, 13, 15, 108548, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='requiest_list',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 7, 13, 15, 108511, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 7, 13, 15, 69109, tzinfo=utc)),
        ),
    ]