# Generated by Django 3.0.6 on 2020-06-16 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0002_to_do_usr_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do',
            name='usr_id',
            field=models.CharField(max_length=255),
        ),
    ]
