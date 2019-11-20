from django.contrib import admin
from . import models


# Register your models here.


class User_Data_formate(admin.ModelAdmin):
    list_display = ('id', 'name', 'mobile_no', 'creation_date')


class Post_Data_formate(admin.ModelAdmin):
    list_display = ('id', 'posted_by', 'posted_on', 'text')


# class Like_Data_formate(admin.ModelAdmin):
#     list_display = ('id', 'post' 'liked_by', 'date_time')


# class Comments_Data_formate(admin.ModelAdmin):
#     list_display = ('id', 'post' 'comments_by', 'comment' 'date_time')


class Request_Data_formate(admin.ModelAdmin):
    list_display = ('id', 'requested_by', 'requested_to',
                    'date_time', 'status', 'accept_date')


admin.site .register(models.User_data, User_Data_formate)
admin.site .register(models.Posted_data, Post_Data_formate)
admin.site .register(models.Likes)
admin.site .register(models.Comments)
admin.site .register(models.Requiest_list, Request_Data_formate)
admin.site .register(models.OTP)
