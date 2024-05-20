from django.urls import re_path
from apps.User.views import AuthorizationViewAPI, RegistrationViewAPI, logout_view


urlpatterns = [
    re_path('login/', AuthorizationViewAPI.as_view()),
    re_path('signup/', RegistrationViewAPI.as_view()),
    re_path('logout/', logout_view),
]