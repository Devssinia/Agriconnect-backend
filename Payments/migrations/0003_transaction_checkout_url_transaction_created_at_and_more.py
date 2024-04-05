# Generated by Django 4.2.3 on 2024-04-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0002_remove_transaction_checkout_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='checkout_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='phone_no',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
