from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('schedule', views.schedule),
    path('clients', views.clientlist),
    path('clients/synopsis', views.clientSynopsis),
    path('clients/address', views.clientAddress),
    path('appointments', views.appointment),
    path('appointments/remove', views.removeAppointment)
]
