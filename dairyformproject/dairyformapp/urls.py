from django.urls import path
from dairyformapp.views import FarmerList

urlpatterns = [
    path('Farmer/', FarmerList.as_view()),
]
