# Generated by Django 3.0.6 on 2020-06-18 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usr_id',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
