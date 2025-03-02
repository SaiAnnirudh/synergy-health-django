from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Patient Details
    path('patient_details/', views.patient_details, name='patient_details'),

    # BMI Calculator
    path('bmi_calculator/', views.bmi_calculator, name='bmi_calculator'),

    # Weight Tracker
    path('weight_tracker/', views.weight_tracker, name='weight_tracker'),

    # Height Tracker
    path('height_tracker/', views.height_tracker, name='height_tracker'),

    # Nutritional Plan
    path('nutritional_plan/', views.nutritional_plan, name='nutritional_plan'),
]