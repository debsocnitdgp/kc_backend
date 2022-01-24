# Generated by Django 2.2.4 on 2022-01-24 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundNo', models.IntegerField(default=1)),
                ('participant1', models.CharField(blank=True, max_length=200)),
                ('participant1_email', models.EmailField(blank=True, max_length=254)),
                ('participant2', models.CharField(blank=True, max_length=200)),
                ('participant2_email', models.EmailField(blank=True, max_length=254)),
                ('participant3', models.CharField(blank=True, max_length=200)),
                ('participant3_email', models.EmailField(blank=True, max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
