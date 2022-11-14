from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar')
]