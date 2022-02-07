# Generated by Django 4.0.2 on 2022-02-07 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TPMSDEVICE1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('tyre1', models.IntegerField()),
                ('tyre2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TPMSDEVICE2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('tyre3', models.IntegerField()),
                ('tyre4', models.IntegerField()),
            ],
        ),
    ]