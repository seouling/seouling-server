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
    login_type = models.CharField(max_length=30)
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_authenticated = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}: {self.nickname}"

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
    morning = models.ManyToManyField('Spot', related_name="morning")
    after_noon = models.ManyToManyField('Spot', related_name="after_noon")
    night = models.ManyToManyField('Spot', related_name="night")


class Spot(models.Model):
    gu = models.IntegerField(default=0)
    category = models.IntegerField(default=0)
    kr_name = models.CharField(max_length=100, unique=True)
    en_name = models.CharField(max_length=100, unique=True)
    kr_content = models.TextField()
    en_content = models.TextField()
    kr_operation = models.CharField(max_length=50)
    en_operation = models.CharField(max_length=50)
    recommend_time = models.CharField(max_length=30)
    kr_subway = models.CharField(max_length=30)
    en_subway = models.CharField(max_length=30)
    line = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    homepage = models.CharField(max_length=100)
    kr_address = models.CharField(max_length=100)
    en_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}.{self.kr_name}({self.en_name})"


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
    picture = models.CharField(max_length=100)


class SpotTag(models.Model):
    spot = models.ForeignKey(Spot, related_name="tags", on_delete=models.CASCADE)
    tag_id = models.IntegerField()


class Comment(models.Model):
    spot = models.ForeignKey('Spot', related_name="comments", on_delete=models.CASCADE)
    writer = models.ForeignKey('User', related_name="comments", on_delete=models.PROTECT)
    content = models.TextField()
    score = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    spot = models.ForeignKey('Spot', related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name="likes", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)


class Visit(models.Model):
    spot = models.ForeignKey('Spot', related_name="visits", on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name="visits", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
