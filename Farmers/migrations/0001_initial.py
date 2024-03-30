# Generated by Django 4.2.3 on 2024-03-30 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_no', models.CharField(max_length=20)),
                ('location_latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('location_name', models.CharField(max_length=255)),
                ('profile_image', models.CharField(max_length=255)),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.customuser')),
            ],
        ),
    ]
