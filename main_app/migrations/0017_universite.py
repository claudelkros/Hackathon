# Generated by Django 2.1.3 on 2019-03-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_ecole'),
    ]

    operations = [
        migrations.CreateModel(
            name='Universite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='file/')),
                ('description', models.TextField(max_length=150000)),
                ('date_pubication', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
