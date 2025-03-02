from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class BMI(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    height = models.FloatField()  # Height in centimeters
    weight = models.FloatField()  # Weight in kilograms
    bmi = models.FloatField()    # BMI value
    date = models.DateField(auto_now_add=True)  # Date of calculation

    def __str__(self):
        return f"{self.patient.name} - {self.bmi}"

class WeightTracker(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()

class HeightTracker(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    height = models.FloatField()

class NutritionalPlan(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    plan = models.TextField()