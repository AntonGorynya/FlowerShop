# Generated by Django 4.2.4 on 2023-08-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_bouquet_consist_bouquet_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='имя')),
                ('phone', models.CharField(max_length=300, verbose_name='телефон')),
            ],
        ),
    ]