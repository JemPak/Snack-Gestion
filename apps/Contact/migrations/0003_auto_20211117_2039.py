# Generated by Django 3.2.7 on 2021-11-18 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_alter_contact_assesory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(blank=True, max_length=600, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name='Date_create'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_response',
            field=models.DateField(auto_now_add=True, verbose_name='Date_response'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]
