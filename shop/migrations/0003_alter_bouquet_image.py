# Generated by Django 4.2.4 on 2023-08-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_bouquet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='image',
            field=models.ImageField(upload_to='bouquets', verbose_name='фото'),
        ),
    ]