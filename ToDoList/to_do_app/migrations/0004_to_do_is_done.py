# Generated by Django 3.0.6 on 2020-06-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0003_auto_20200616_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='to_do',
            name='is_done',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
