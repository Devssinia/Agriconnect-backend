# Generated by Django 5.0.3 on 2024-03-30 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Farmers', '0002_rename_farmer_farmers_farmerproducts'),
        ('Products', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('currency', models.CharField(max_length=3)),
                ('amount', models.DecimalField(decimal_places=6, max_digits=9)),
                ('status', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.DecimalField(decimal_places=6, max_digits=9)),
                ('farm_product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farmers.farmerproducts')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_duration', models.DecimalField(decimal_places=6, max_digits=9)),
                ('deliver_distance', models.DecimalField(decimal_places=6, max_digits=9)),
                ('is_delivered', models.BooleanField(default=False)),
                ('date_of_delivery', models.DateTimeField()),
                ('expected_delivery_date', models.DateTimeField()),
                ('signiture', models.CharField()),
                ('delivery_address_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('delivery_address_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('delivery_address_name', models.CharField()),
                ('merchant_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.customuser')),
                ('total_amount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.categories')),
            ],
        ),
    ]
