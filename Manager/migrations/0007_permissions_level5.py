# Generated by Django 3.2.9 on 2021-12-31 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0006_alter_owner_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissions',
            name='level5',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=3),
            preserve_default=False,
        ),
    ]
