# Generated by Django 4.2.3 on 2024-04-01 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location_latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location_longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='location_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_image',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.role'),
        ),
    ]
