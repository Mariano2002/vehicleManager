# Generated by Django 3.2.9 on 2021-12-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='owner_account',
            new_name='owner',
        ),
    ]