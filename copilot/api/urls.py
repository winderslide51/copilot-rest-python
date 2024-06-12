
from django.urls import path

from . import views

urlpatterns = [
    path('time/', views.get_current_time),
]
