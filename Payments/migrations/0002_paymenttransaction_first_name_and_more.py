# Generated by Django 4.2.3 on 2024-04-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransaction',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='paymenttransaction',
            name='method',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransaction',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
