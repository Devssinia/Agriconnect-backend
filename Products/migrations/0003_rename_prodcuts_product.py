# Generated by Django 4.2.3 on 2024-04-04 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmers', '0003_rename_farmers_farmer'),
        ('Products', '0002_alter_prodcuts_product_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Prodcuts',
            new_name='Product',
        ),
    ]
