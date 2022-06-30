from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('raihan_app/', include("raihan_app.urls") ),
    path('admin/', admin.site.urls),
]
