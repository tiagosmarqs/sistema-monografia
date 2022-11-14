from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('buscar/', views.buscar, name='buscar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('deletar/<int:id>', views.deletar, name='deletar')
]