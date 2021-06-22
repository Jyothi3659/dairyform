from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dairyformapp/', include('dairyformapp.urls')),
    path('admin/', admin.site.urls),
]
