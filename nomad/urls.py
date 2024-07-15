
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('nomadApp.urls')),
    path('admin/', admin.site.urls),
    path("api/", include("djoser.urls")),
    path("api/", include("accounts.urls")),
]
