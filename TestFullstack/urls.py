from django.urls import path
from TestFullstack import views

urlpatterns = [
    path('submit', views.Regis.as_view(), name="sumbit_data"),
]