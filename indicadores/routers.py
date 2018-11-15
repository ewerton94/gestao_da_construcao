from rest_framework import routers
from .viewsets import ClienteViewSet, EmpresaViewSet, UserViewSet, EmpreendimentoViewSet, ReferenciaViewSet, TipoIndicadorViewSet, IndicadorViewSet, ResultadoViewSet

router = routers.DefaultRouter()

router.register('clientes', ClienteViewSet, base_name='cliente')
router.register('empresas', EmpresaViewSet, base_name='empresa')
router.register('empreendimentos', EmpreendimentoViewSet, base_name='empreendimento')
router.register('referencias', ReferenciaViewSet, base_name='referencia')
router.register('tipoindicadores', TipoIndicadorViewSet, base_name='tipoindicador')
router.register('indicadores', IndicadorViewSet, base_name='indicador')
router.register('resultados', ResultadoViewSet, base_name='resultado')
