from rest_framework import serializers
from .models import TPMSDEVICE1,TPMSDEVICE2

class TPMSDEVICE1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TPMSDEVICE1
        fields = ('device_name','tyre1','tyre2')
class TPMSDEVICE2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TPMSDEVICE2
        fields = ('device_name','tyre3','tyre4')