# Generated by Django 2.1 on 2020-02-24 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='fact',
            new_name='news',
        ),
    ]
