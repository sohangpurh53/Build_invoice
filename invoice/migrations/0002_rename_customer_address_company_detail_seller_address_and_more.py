# Generated by Django 4.1.5 on 2023-02-23 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_detail',
            old_name='customer_address',
            new_name='seller_address',
        ),
        migrations.RenameField(
            model_name='company_detail',
            old_name='customer_name',
            new_name='seller_name',
        ),
    ]
