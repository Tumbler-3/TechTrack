from django.db import models
from apps.Equipment.models import Equipment

# Create your models here.
class Data(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='equipment_data')
    temperature = models.IntegerField()
    speed = models.IntegerField()
    pressure = models.IntegerField()
    
    def __str__(self):
        return f'{self.equipment.model} data'

    class Meta:
        verbose_name = 'Data',
        verbose_name_plural = 'Data'