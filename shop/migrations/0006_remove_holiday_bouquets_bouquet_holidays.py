# Generated by Django 4.2.4 on 2023-08-23 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_holiday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='bouquets',
        ),
        migrations.AddField(
            model_name='bouquet',
            name='holidays',
            field=models.ManyToManyField(to='shop.holiday', verbose_name='подходит для праздников:'),
        ),
    ]
