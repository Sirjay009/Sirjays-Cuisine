# Generated by Django 4.2.17 on 2025-01-04 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0011_remove_reservation_email_remove_reservation_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(default='Guest', max_length=100),
            preserve_default=False,
        ),
    ]
