# Generated by Django 2.0 on 2017-12-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20171213_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribe',
            field=models.BooleanField(default=False),
        ),
    ]