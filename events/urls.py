from django.urls import path
from .views import register_event, registration_success


urlpatterns = [
    path('', register_event, name='register_event'),
    path('success/', registration_success, name='registration_success'),
]