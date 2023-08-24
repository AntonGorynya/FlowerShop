# Generated by Django 4.2.4 on 2023-08-23 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_order_period'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='наименование праздника')),
                ('bouquets', models.ManyToManyField(to='shop.bouquet')),
            ],
        ),
    ]