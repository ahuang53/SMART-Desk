from django.db import models

# Create your models here.

# class SensorReading(models.Model):
#     rfid = models.CharField(max_length=50)
#     left_weight = models.FloatField(default = 0.0)
#     right_weight = models.FloatField(default = 0.0)
#     distance = models.FloatField()
#     timestamp = models.DateTimeField(auto_now_add=True)

class DistanceReading(models.Model):
    value = models.FloatField(default = 0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

class WeightReading(models.Model):
    left = models.FloatField(default = 0.0)
    right = models.FloatField(default = 0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

class RFIDReading(models.Model):
    mode = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)