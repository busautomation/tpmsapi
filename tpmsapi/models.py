from django.db import models

# Create your models here.
class TPMSDEVICE1(models.Model):
    device_name=models.CharField(max_length=100)
    tyre1=models.IntegerField()
    tyre2=models.IntegerField()
    
    def __str__(self):
        return self.device_name
class TPMSDEVICE2(models.Model):
    device_name=models.CharField(max_length=100)
    tyre3=models.IntegerField()
    tyre4=models.IntegerField()
    
    def __str__(self):
        return self.device_name