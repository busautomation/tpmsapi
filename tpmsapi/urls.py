from os import urandom
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

Router = DefaultRouter()
Router.register('tpmsdevice1',views.TPMSDEVICE1ViewSet)
Router.register('tpmsdevice2',views.TPMSDEVICE2ViewSet)

urlpatterns = [
    path('',include(Router.urls)),
]

