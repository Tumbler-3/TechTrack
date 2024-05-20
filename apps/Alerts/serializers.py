from rest_framework import serializers
from apps.Alerts.models import Alerts


class AlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'
        
    equipment_name = serializers.SerializerMethodField()
    
    def get_equipment_name(self, obj):
        return f'{obj.equipment.model}'