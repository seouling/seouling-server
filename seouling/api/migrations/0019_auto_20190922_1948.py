# Generated by Django 2.2.4 on 2019-09-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20190922_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotpicture',
            name='picture',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]