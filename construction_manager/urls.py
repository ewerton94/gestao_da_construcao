"""construction_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from indicadores.routers import router
from indicadores.views import form_empresas, form_editar_empresas, criar_empreendimento
from indicadores.views import form_indicadores, visualizar_resultados
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('form_indicadores/', form_indicadores, name="form_indicadores"),
    path('visualizar_resultados/', visualizar_resultados, name="visualizar_resultados"),
    path('form_empresas/', form_empresas, name="form_empresas"),
    path('form_empresas/<int:id>', form_editar_empresas, name="form_editar_empresas"),
    path('criar_empreendimento/', criar_empreendimento, name="form_empresas"),
    path('form_empreendimentos/<int:id>', form_editar_empresas, name="form_editar_empresas"),

]

urlpatterns += router.urls