from django.contrib import admin
from .models import Empresa, Cliente, Pesquisador, Resultado, Indicador, Empreendimento, Referencia, TipoIndicador, CampoIndicador

admin.site.register(Empresa)
admin.site.register(CampoIndicador)
admin.site.register(Empreendimento)
admin.site.register(Cliente)
admin.site.register(Pesquisador)
admin.site.register(Referencia)
admin.site.register(TipoIndicador)
admin.site.register(Indicador)
admin.site.register(Resultado)
