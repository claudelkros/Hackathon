# Generated by Django 2.1.3 on 2019-03-15 09:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_auto_20190315_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroCarnet', models.CharField(max_length=12)),
                ('nomPatient', models.CharField(max_length=200)),
                ('alergie', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=100)),
                ('numberEmergency', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.timedelta)),
                ('traitement', models.CharField(max_length=500)),
                ('observation', models.CharField(max_length=500)),
                ('analyse', models.CharField(max_length=400)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomculture', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('guide', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Maladie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nommaladie', models.CharField(max_length=100)),
                ('symtome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Memoire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('filiere', models.CharField(max_length=100)),
                ('annee', models.CharField(max_length=15)),
                ('niveau', models.IntegerField(default=15)),
                ('redacteur', models.CharField(max_length=300)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomplante', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('maladie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Maladie')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproduit', models.CharField(max_length=100)),
                ('prix', models.CharField(max_length=50)),
                ('numvendeur', models.IntegerField(default=15)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='carnet',
            name='consultation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Consultation'),
        ),
        migrations.AddField(
            model_name='carnet',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
