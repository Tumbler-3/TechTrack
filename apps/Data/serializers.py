from rest_framework import serializers
from apps.Data.models import Data


class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = '__all__'
        
    equipment_name = serializers.SerializerMethodField()
    
    def get_equipment_name(self, obj):
        return f'{obj.equipment.model}'
