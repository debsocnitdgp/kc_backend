# Generated by Django 2.2.4 on 2022-01-25 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20220125_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='roundNo',
        ),
    ]