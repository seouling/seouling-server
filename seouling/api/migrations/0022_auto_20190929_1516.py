# Generated by Django 2.2.4 on 2019-09-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190927_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='spot',
            name='x_pos',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='spot',
            name='y_pos',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
