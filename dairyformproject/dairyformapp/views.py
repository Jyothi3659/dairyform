from django.shortcuts import render
from django.views.generic import ListView
from dairyformapp.models import Farmer

class FarmerList(ListView):
    model = Farmer