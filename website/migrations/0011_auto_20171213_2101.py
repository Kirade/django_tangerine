# Generated by Django 2.0 on 2017-12-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20171213_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='visit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='board',
            name='writer',
            field=models.CharField(max_length=20),
        ),
    ]