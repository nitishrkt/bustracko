# Generated by Django 2.2.11 on 2020-03-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]