# Generated by Django 3.2.7 on 2021-11-23 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Installation', '0004_auto_20211117_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='installation',
            name='machine_type',
            field=models.CharField(choices=[(0, 'Granos'), (1, 'Granos chicos'), (2, 'Mayor capacidad'), (3, 'Maquina estandar')], max_length=50, null=True, verbose_name='Machine_type'),
        ),
        migrations.AlterField(
            model_name='installation',
            name='user_id',
            field=models.BigIntegerField(null=True, verbose_name='user_id'),
        ),
    ]