from django.urls import path
from . import views

urlpatterns = [
    path('sendRequest', views.activate),
    path('setStatus', views.change_status)
]