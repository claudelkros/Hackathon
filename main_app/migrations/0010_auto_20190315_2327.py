# Generated by Django 2.1.3 on 2019-03-15 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20190315_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='titre',
            field=models.CharField(max_length=500),
        ),
    ]
