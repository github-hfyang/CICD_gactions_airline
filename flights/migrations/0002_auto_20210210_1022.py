# Generated by Django 3.1.5 on 2021-02-10 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='flights',
            new_name='Flight',
        ),
    ]
