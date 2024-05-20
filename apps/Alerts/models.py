from django.db import models
from apps.Equipment.models import Equipment
# Create your models here.


class Alerts(models.Model):
    choices = {'Safe': 'Safe', 'Warning': 'Warning', 'Danger': 'Danger'}

    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='equipment_alerts')
    situation = models.CharField(choices=choices, max_length=20)
    desc = models.TextField(null=True, blank=True)
    timestamp = models.TimeField()
    
    def __str__(self):
        return f'{self.equipment.model} alerts'

    class Meta:
        verbose_name = 'Alerts',
        verbose_name_plural = 'Alerts'
