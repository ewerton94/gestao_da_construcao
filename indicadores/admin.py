from django.contrib import admin
from .models import Empresa, Cliente, Pesquisador, Resultado, Indicador, Empreendimento, Referencia, TipoIndicador, CampoIndicador, TCPO, RegitroErrosEnvios, LogEnvioDeResultado

class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('indicador', 'campo_indicador', 'referencia', 'referencia')
    list_filter = ('empreendimento', 'indicador', 'referencia', 'referencia')

class LogEnvioDeResultadoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'empreendimento')
    list_filter = ('referencia', 'empreendimento')

class RegitroErrosEnviosAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'empreendimento')
    list_filter = ('referencia', 'empreendimento')


admin.site.register(Empresa)
admin.site.register(CampoIndicador)
admin.site.register(Empreendimento)
admin.site.register(Cliente)
admin.site.register(Pesquisador)
admin.site.register(Referencia)
admin.site.register(TipoIndicador)
admin.site.register(Indicador)
admin.site.register(Resultado, ResultadoAdmin)
admin.site.register(LogEnvioDeResultado, LogEnvioDeResultadoAdmin)
admin.site.register(RegitroErrosEnvios, RegitroErrosEnviosAdmin)
admin.site.register(TCPO)