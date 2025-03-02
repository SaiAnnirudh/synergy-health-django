from django import forms
from .models import Patient, BMI, WeightTracker, HeightTracker, NutritionalPlan

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender']

class BMIForm(forms.ModelForm):
    class Meta:
        model = BMI
        fields = ['height', 'weight']  # Height in cm, weight in kg

class WeightTrackerForm(forms.ModelForm):
    class Meta:
        model = WeightTracker
        fields = ['date', 'weight']

class HeightTrackerForm(forms.ModelForm):
    class Meta:
        model = HeightTracker
        fields = ['date', 'height']

class NutritionalPlanForm(forms.ModelForm):
    class Meta:
        model = NutritionalPlan
        fields = ['plan']