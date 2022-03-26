from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addData),
]