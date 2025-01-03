# Generated by Django 4.2.17 on 2024-12-26 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='table',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
