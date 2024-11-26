from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio/', views.inicio, name='inicio'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('analista/', views.analista, name='analista'),
    path('Proveedores/', views.proveedores, name='Proveedores'),
    path('dashboard-form/', views.dashboard, name='dashboardForm'),
    path('dashboard-form-2/', views.dashboard_form_2, name='dashboardForm2'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    
]