# Generated by Django 4.2.4 on 2023-08-24 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_bouquet_name_alter_bouquet_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='holidays',
            field=models.ManyToManyField(related_name='bouquets', to='shop.holiday', verbose_name='подходит для праздников:'),
        ),
    ]
