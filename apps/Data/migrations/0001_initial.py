# Generated by Django 5.0 on 2024-05-18 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_data', to='Equipment.equipment')),
            ],
            options={
                'verbose_name': ('Data',),
                'verbose_name_plural': 'Data',
            },
        ),
    ]
