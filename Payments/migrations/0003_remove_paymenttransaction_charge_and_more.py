# Generated by Django 5.0.3 on 2024-04-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Payments', '0002_paymenttransaction_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='checkout_url',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='currency',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='email',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='method',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='status',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='tx_ref',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='type',
        ),
        migrations.RemoveField(
            model_name='paymenttransaction',
            name='updated_at',
        ),
    ]