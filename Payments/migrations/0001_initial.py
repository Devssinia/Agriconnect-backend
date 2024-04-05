# Generated by Django 4.2.3 on 2024-04-05 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('currency', models.CharField(default='ETB', max_length=255)),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('phone_no', models.CharField(max_length=255, null=True)),
                ('charge', models.CharField(max_length=255, null=True)),
                ('mode', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('tx_ref', models.CharField(max_length=255)),
                ('checkout_url', models.URLField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
