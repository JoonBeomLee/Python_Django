# Generated by Django 3.0.6 on 2020-06-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0004_to_do_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='to_do',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]