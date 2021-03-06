# Generated by Django 2.2.4 on 2019-09-26 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190922_2000'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('spot', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='spottag',
            unique_together={('spot', 'tag_id')},
        ),
        migrations.AlterUniqueTogether(
            name='visit',
            unique_together={('spot', 'user')},
        ),
    ]
