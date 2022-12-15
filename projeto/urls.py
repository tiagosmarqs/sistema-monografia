"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from projeto.api import viewsets

router = routers.DefaultRouter()

router.register(r'autor', viewsets.AutorViewSet, basename="Autor")
router.register(r'orientador', viewsets.OrientadorViewSet, basename="Orientador")
router.register(r'coorientador', viewsets.CoorientadorViewSet, basename="Coorientador")
router.register(r'monografia', viewsets.MonografiaViewSet, basename="Monografia")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('monografia/', permanent=False)),
    path('autor/', include('autor.urls')),
    path('orientador/', include('orientador.urls')),
    path('coorientador/', include('coorientador.urls')),
    path('monografia/', include('monografia.urls')),
    path('api/', include(router.urls)),
]
