from django.db import models
from django.utils import timezone
# Create your models here.


class User_data(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'
    GENDER_IN_CHOICES = [
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER'),
    ]
    name = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10, choices=GENDER_IN_CHOICES, default="")
    mobile_no = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=20)
    image = models.ImageField(default='default.png',upload_to='images/')
    creation_date = models.DateTimeField(default=timezone.now())
    Isverify = models.BooleanField(default=False)


class OTP(models.Model):
    mobile_no = models.CharField(max_length=12)
    otp = models.CharField(max_length=5)
    time=models.DateTimeField(default=timezone.now())


class Posted_data(models.Model):
    posted_by = models.ForeignKey(User_data, on_delete=models.CASCADE)
    posted_on = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True)
    text = models.TextField(max_length=None, blank=True)
    likes_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    # isilike = models.BooleanField(default=False)
    # updation_date = models.DateTimeField()

    # def likes(self):
    #     Li = like.objects


class Likes(models.Model):
    post = models.ForeignKey(Posted_data, on_delete=models.CASCADE)
    liked_by = models.ForeignKey(User_data, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now())


class Comments(models.Model):
    post = models.ForeignKey(Posted_data, on_delete=models.CASCADE)
    comments_by = models.ForeignKey(User_data, on_delete=models.CASCADE)
    comment = models.TextField(max_length=None, blank=True)
    date_time = models.DateTimeField(default=timezone.now())


class Requiest_list(models.Model):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'
    UNFRIEND = 'UNFRIEND'
    STATUS_CHOICES = [
        (PENDING, 'PENDING'),
        (ACCEPTED, 'ACCEPTED'),
        (REJECTED, 'REJECTED'),
        (UNFRIEND, 'UNFRIEND'),
    ]
    requested_by = models.ForeignKey(
        User_data, on_delete=models.CASCADE, related_name='creator')
    # requested_to = models.CharField(max_length=10)
    requested_to = models.ForeignKey(
        User_data, on_delete=models.CASCADE, related_name='assignee')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=PENDING)
    date_time = models.DateTimeField(default=timezone.now())
    accept_date = models.DateTimeField(default=timezone.now())

# class like(models.Model):
