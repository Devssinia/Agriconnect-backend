# Generated by Django 5.0.3 on 2024-04-03 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_rename_otp_expiry_customuser_otp_expirty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='otp_expirty',
            new_name='otp_expiry',
        ),
    ]