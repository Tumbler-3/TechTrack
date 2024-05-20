from django.urls import path
from apps.Alerts.views import AlertsViewAPI, AlertsDetailViewAPI


urlpatterns = [
    path('alerts/', AlertsViewAPI.as_view()),
    path('alerts/<int:id>/', AlertsDetailViewAPI.as_view()),
]
