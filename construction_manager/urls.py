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
from indicadores.views import form_indicadores, visualizar_resultados, criar_codigos
from indicadores.views import form_empresas, form_editar_empresas, criar_empreendimento, editar_empreendimento, criar_cliente, editar_cliente, criar_user, editar_user, criar_referencia, editar_referencia, criar_indicador, editar_indicador, criar_tipoindicador, editar_tipoindicador, criar_resultado, editar_resultado, criar_pesquisador, editar_pesquisador

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('form_indicadores/', form_indicadores, name="form_indicadores"),
    path('visualizar_resultados/', visualizar_resultados, name="visualizar_resultados"),
    path('form_empresas/', form_empresas, name="form_empresas"),
    path('form_empresas/<int:id>', form_editar_empresas, name="form_editar_empresas"),
    path('criar_empreendimento/', criar_empreendimento, name="criar_empreendimento"),
    path('editar_empreendimento/<int:id>', editar_empreendimento, name="editar_empreendimento"),
    path('criar_codigos/', criar_codigos, name="criar_codigos"),
    path('criar_cliente/', criar_cliente, name="criar_cliente"),
    path('editar_cliente/<int:id>', editar_cliente, name="editar_cliente"),
    path('criar_user/', criar_user, name="criar_user"),
    path('editar_user/<int:id>', editar_user, name="editar_user"),
    path('criar_referencia/', criar_referencia, name="criar_referencia"),
    path('editar_referencia/<int:id>', editar_referencia, name="editar_referencia"),
    path('criar_indicador/', criar_indicador, name="criar_indicador"),
    path('editar_indicador/<int:id>', editar_indicador, name="editar_indicador"),
    path('criar_tipoindicador/', criar_tipoindicador, name="criar_tipoindicador"),
    path('editar_tipoindicador/<int:id>', editar_tipoindicador, name="editar_tipoindicador"),
    path('criar_resultado/', criar_resultado, name="criar_resultado"),
    path('editar_resultado/<int:id>', editar_resultado, name="editar_resultado"),
    path('criar_pesquisador/', criar_pesquisador, name="criar_pesquisador"),
    path('editar_pesquisador/<int:id>', editar_pesquisador, name="editar_pesquisador"),

]

urlpatterns += router.urls
