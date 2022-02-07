import re
from django.shortcuts import render
from .models import TPMSDEVICE1,TPMSDEVICE2
from .serializer import TPMSDEVICE1Serializer,TPMSDEVICE2Serializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class TPMSDEVICE1ViewSet(viewsets.ModelViewSet):
    queryset = TPMSDEVICE1.objects.all()
    serializer_class = TPMSDEVICE1Serializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class TPMSDEVICE2ViewSet(viewsets.ModelViewSet):
    queryset = TPMSDEVICE2.objects.all()
    serializer_class = TPMSDEVICE2Serializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, *args, **kwargs)
