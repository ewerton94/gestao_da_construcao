from django.contrib import admin
from .models import Empresa, Cliente, Pesquisador, Indicador, Empreendimento, Referencia, TipoIndicador

admin.site.register(Empresa)
admin.site.register(Empreendimento)
admin.site.register(Cliente)
admin.site.register(Pesquisador)
admin.site.register(Referencia)
admin.site.register(TipoIndicador)
admin.site.register(Indicador)
