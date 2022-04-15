# Generated by Django 3.2.6 on 2022-02-18 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('username', models.CharField(max_length=250, verbose_name='Username')),
                ('number', models.IntegerField(default=0, verbose_name='Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 2, 18, 11, 59, 53, 863177, tzinfo=utc), verbose_name='Time')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedback',
            },
        ),
    ]
