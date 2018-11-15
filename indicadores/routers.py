from rest_framework import routers
from .viewsets import ClienteViewSet, EmpresaViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('clientes', ClienteViewSet, base_name='cliente')
router.register('empresas', EmpresaViewSet, base_name='empresa')
router.register('users', UserViewSet, base_name='user')