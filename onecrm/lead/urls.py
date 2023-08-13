from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.LeadListview.as_view() , name='list'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='delete'),
    path('<int:pk>/edit/', views.LeadUpdateView.as_view(), name='edit'),
    path('<int:pk>/convert/', views.ConvertToClient.as_view(), name='convert'),
    path('add/', views.LeadCreateView.as_view(), name='add' ),
]