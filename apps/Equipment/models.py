from django.db import models

# Create your models here.

class Equipment(models.Model):
    model = models.CharField(max_length=70)
    eq_type = models.CharField(max_length=70)
    inst_date = models.DateField()
    status = models.CharField(max_length=70)
    
    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Equipment',
        verbose_name_plural = 'Equipments'
    