from django.db import models


def user_profile_upload(instance, filename):
    """
    e.g)
        images/user/{user_id}/{filename}
        images/user/122/tmp.png
    """
    path = "images/user/{}/{}".format(instance.id, filename)
    return path


class User(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to=user_profile_upload, null=True)
    email = models.CharField(max_length=50, null=True, unique=True)
    password = models.TextField(null=True)
    token = models.CharField(max_length=100, db_index=True)
    sns_token = models.CharField(max_length=100, null=True, unique=True)
    is_push = models.BooleanField(default=True)
    login_type = models.IntegerField() # 0: email, 1: facebook, 2: kakao, 3: google
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.profile_picture
            self.profile_picture = None
            super(User, self).save(*args, **kwargs)
            self.profile_picture = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(User, self).save(*args, **kwargs)


class Plan(models.Model):
    user = models.ForeignKey(User, related_name="plans", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


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


def spot_image_upload(instance, filename):
    """
    e.g)
        images/spot/{spot_id}/{filename}
        images/spot/123/tmp.png
    """
    path = "images/spot/{}/{}".format(instance.id, filename)
    return path


class SpotPicture(models.Model):
    spot = models.ForeignKey('Spot', related_name='pictures', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=spot_image_upload, null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.picture
            self.picture = None
            super(SpotPicture, self).save(*args, **kwargs)
            self.picture = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')

        super(SpotPicture, self).save(*args, **kwargs)


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
