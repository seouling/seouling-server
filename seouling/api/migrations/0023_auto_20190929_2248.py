# Generated by Django 2.2.4 on 2019-09-29 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20190929_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spot',
            old_name='x_pos',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='spot',
            old_name='y_pos',
            new_name='lng',
        ),
    ]