from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('backend.base.urls')),
    path('admin/', admin.site.urls),
]
