from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'logs', views.LogViewSet)

urlpatterns = [
    path('messages', views.messages, name='messages'),
    path('audios', views.audios, name='audios'),
    path('start', views.start, name='start'),
    path('', include(router.urls))
]
