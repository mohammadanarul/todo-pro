# Generated by Django 4.1.1 on 2022-09-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskDescription',
            new_name='TaskReport',
        ),
    ]
