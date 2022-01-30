# Generated by Django 2.2.4 on 2022-01-30 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20220130_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Round')),
            ],
        ),
    ]