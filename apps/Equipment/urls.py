from django.urls import path
from apps.Equipment.views import EquipmentViewAPI,EquipmentDetailViewAPI


urlpatterns = [
    path('equipment/', EquipmentViewAPI.as_view()),
    path('equipment/<int:id>/', EquipmentDetailViewAPI.as_view()),
]
