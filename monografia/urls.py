from django.urls import path
from . import views

urlpatterns =[
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('buscar/', views.buscar, name='buscar')
]