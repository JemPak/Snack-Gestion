# Generated by Django 3.2.7 on 2021-11-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('installation_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(verbose_name='user_id')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('machine_type', models.CharField(choices=[('Granos', 'Granos'), ('Granos chicos', 'Granos chicos'), ('Mayor capacidad', 'Mayor capacidad'), ('Maquina estandar', 'Maquina estandar')], max_length=50, verbose_name='Machine_type')),
                ('accepted', models.BooleanField(verbose_name='Accepted')),
                ('response', models.TextField(blank=True, max_length=600, null=True, verbose_name='Response')),
                ('date_create', models.DateField(verbose_name='Date_create')),
                ('date_response', models.DateField(verbose_name='Date_response')),
            ],
        ),
    ]
