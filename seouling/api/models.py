from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    profile_picture = models.TextField(null=True)
    email = models.CharField(max_length=50, null=True, unique=True)
    password = models.TextField(null=True)
    token = models.CharField(max_length=100, unique=True)
    sns_token = models.CharField(max_length=100, null=True, unique=True)
    is_push = models.BooleanField(default=True)
    login_type = models.IntegerField() # 0: email, 1: facebook, 2: kakao, 3: google
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Plan(models.Model):
    user = models.ForeignKey(User, related_name="plans", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    picture = models.TextField()
    is_main = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()


class Schedule(models.Model):
    plan = models.ForeignKey(Plan, related_name='schedules', on_delete=models.CASCADE)
    date = models.DateField()
    order = models.IntegerField()
    morning = models.ManyToManyField('Spot', related_name="morning")
    after_noon = models.ManyToManyField('Spot', related_name="after_noon")
    night = models.ManyToManyField('Spot', related_name="night")


class Spot(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    district = models.CharField(max_length=20)
    # other fields...


class SpotPicture(models.Model):
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    url = models.CharField(max_length=50)


class Comment(models.Model):
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    writer = models.ForeignKey('User', on_delete=models.PROTECT)
    content = models.TextField()


class Like(models.Model):
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.PROTECT)


class Visit(models.Model):
    spot = models.ForeignKey('Spot', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
