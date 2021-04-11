from django.contrib import admin
from django.urls import path, include
from .views import Graph

urlpatterns = [
    
    path('plotly/company/<str:company>', Graph.as_view(), name="companypage"),
]