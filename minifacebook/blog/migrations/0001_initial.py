# Generated by Django 2.2.5 on 2019-11-11 10:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')], default='', max_length=10)),
                ('mobile_no', models.CharField(max_length=12, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2019, 11, 11, 10, 45, 33, 899946, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Requiest_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_to', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('ACCEPTED', 'ACCEPTED'), ('REGECTED', 'REGECTED'), ('UNFRIEND', 'UNFRIEND')], default='PENDING', max_length=10)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2019, 11, 11, 10, 45, 33, 937546, tzinfo=utc))),
                ('accept_date', models.DateTimeField(default=datetime.datetime(2019, 11, 11, 10, 45, 33, 937584, tzinfo=utc))),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Posted_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_on', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('text', models.TextField(blank=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=datetime.datetime(2019, 11, 11, 10, 45, 33, 935783, tzinfo=utc))),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Posted_data')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2019, 11, 11, 10, 45, 33, 936575, tzinfo=utc))),
                ('comments_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Posted_data')),
            ],
        ),
    ]