from django.urls import path 

from . import views 

app_name = 'dashboard' 
urlpatterns = [
    path('', views.dashbaord , name= 'index'),
]