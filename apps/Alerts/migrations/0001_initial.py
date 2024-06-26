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
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.CharField(choices=[('Safe', 'Safe'), ('Warning', 'Warning'), ('Danger', 'Danger')], max_length=20)),
                ('desc', models.TextField(blank=True, null=True)),
                ('timestamp', models.TimeField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipment_alerts', to='Equipment.equipment')),
            ],
            options={
                'verbose_name': ('Alerts',),
                'verbose_name_plural': 'Alerts',
            },
        ),
    ]
