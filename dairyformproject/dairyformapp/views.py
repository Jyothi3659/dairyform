from django.shortcuts import render
from django.views.generic import Listview
from dairyformapp.models import Farmer

class FarmerList(Listview):
    model = Farmer