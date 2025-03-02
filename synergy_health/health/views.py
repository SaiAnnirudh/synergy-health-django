from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PatientForm, BMIForm, WeightTrackerForm, HeightTrackerForm, NutritionalPlanForm
from .models import Patient, BMI, WeightTracker, HeightTracker, NutritionalPlan

# Home Page
def home(request):
    return render(request, 'health/home.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'health/login.html', {'error': 'Invalid credentials'})
    return render(request, 'health/login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')

# Patient Details View
@login_required
def patient_details(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('home')
    else:
        form = PatientForm()
    return render(request, 'health/patient_details.html', {'form': form})

@login_required
def bmi_calculator(request):
    if request.method == 'POST':
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi = form.save(commit=False)
            try:
                patient = Patient.objects.get(user=request.user)
                bmi.patient = patient
                # Convert height from cm to meters
                height_in_meters = bmi.height / 100
                # Calculate BMI
                bmi.bmi = bmi.weight / (height_in_meters ** 2)
                bmi.save()  # Save the BMI object (including the date field)
                return render(request, 'health/bmi_calculator.html', {
                    'form': form,
                    'bmi': round(bmi.bmi, 2),  # Round to 2 decimal places
                    'status': get_bmi_status(bmi.bmi)  # Get BMI status
                })
            except Patient.DoesNotExist:
                return render(request, 'health/bmi_calculator.html', {
                    'form': form,
                    'error': 'Patient profile not found. Please fill in patient details first.'
                })
    else:
        form = BMIForm()
    return render(request, 'health/bmi_calculator.html', {'form': form})

# Helper function to get BMI status
def get_bmi_status(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obese'
# Weight Tracker View
@login_required
def weight_tracker(request):
    if request.method == 'POST':
        form = WeightTrackerForm(request.POST)
        if form.is_valid():
            weight = form.save(commit=False)
            try:
                patient = Patient.objects.get(user=request.user)
                weight.patient = patient
                weight.save()
                return redirect('weight_tracker')
            except Patient.DoesNotExist:
                return render(request, 'health/weight_tracker.html', {
                    'form': form,
                    'error': 'Patient profile not found. Please fill in patient details first.'
                })
    else:
        form = WeightTrackerForm()
    
    try:
        patient = Patient.objects.get(user=request.user)
        weights = WeightTracker.objects.filter(patient=patient)
    except Patient.DoesNotExist:
        weights = []
    
    return render(request, 'health/weight_tracker.html', {
        'form': form,
        'weights': weights
    })

# Height Tracker View
@login_required
def height_tracker(request):
    if request.method == 'POST':
        form = HeightTrackerForm(request.POST)
        if form.is_valid():
            height = form.save(commit=False)
            try:
                patient = Patient.objects.get(user=request.user)
                height.patient = patient
                height.save()
                return redirect('height_tracker')
            except Patient.DoesNotExist:
                return render(request, 'health/height_tracker.html', {
                    'form': form,
                    'error': 'Patient profile not found. Please fill in patient details first.'
                })
    else:
        form = HeightTrackerForm()
    
    try:
        patient = Patient.objects.get(user=request.user)
        heights = HeightTracker.objects.filter(patient=patient)
    except Patient.DoesNotExist:
        heights = []
    
    return render(request, 'health/height_tracker.html', {
        'form': form,
        'heights': heights
    })

# Nutritional Plan View
@login_required
def nutritional_plan(request):
    if request.method == 'POST':
        form = NutritionalPlanForm(request.POST)
        if form.is_valid():
            plan = form.save(commit=False)
            try:
                patient = Patient.objects.get(user=request.user)
                plan.patient = patient
                plan.save()
                return redirect('nutritional_plan')
            except Patient.DoesNotExist:
                return render(request, 'health/nutritional_plan.html', {
                    'form': form,
                    'error': 'Patient profile not found. Please fill in patient details first.'
                })
    else:
        form = NutritionalPlanForm()
    
    try:
        patient = Patient.objects.get(user=request.user)
        plans = NutritionalPlan.objects.filter(patient=patient)
    except Patient.DoesNotExist:
        plans = []
    
    return render(request, 'health/nutritional_plan.html', {
        'form': form,
        'plans': plans
    })