from django.urls import path
from . import views

urlpatterns = [
    path('messages', views.messages, name='messages'),
    path('audios', views.audios, name='audios'),
    path('start', views.start, name='start'),
]
