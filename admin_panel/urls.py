
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generators/', views.manage_generators, name='manage_generators'),# Your other paths
]
