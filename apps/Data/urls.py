from django.urls import path
from apps.Data.views import DataViewAPI, DataDetailViewAPI


urlpatterns = [
    path('data/', DataViewAPI.as_view()),
    path('data/<int:id>/', DataDetailViewAPI.as_view()),
]
