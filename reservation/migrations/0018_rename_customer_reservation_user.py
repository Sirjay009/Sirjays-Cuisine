# Generated by Django 4.2.17 on 2025-01-07 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0017_rename_user_reservation_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='customer',
            new_name='user',
        ),
    ]