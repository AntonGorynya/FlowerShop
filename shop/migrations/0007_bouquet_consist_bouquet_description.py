# Generated by Django 4.2.4 on 2023-08-24 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_holiday_bouquets_bouquet_holidays'),
    ]

    operations = [
        migrations.AddField(
            model_name='bouquet',
            name='consist',
            field=models.TextField(blank=True, verbose_name='состав'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='description',
            field=models.TextField(blank=True, verbose_name='описание'),
        ),
    ]