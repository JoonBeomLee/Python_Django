# Generated by Django 3.0.6 on 2020-06-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='to_do',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phon_number', models.CharField(max_length=255)),
            ],
        ),
    ]
