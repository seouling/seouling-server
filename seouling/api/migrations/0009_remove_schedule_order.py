# Generated by Django 2.1.5 on 2019-09-08 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190908_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='order',
        ),
    ]