# Generated by Django 3.1.13 on 2021-11-11 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_locations', '0008_auto_20200804_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        )
    ]
