from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartamentoViewSet, MunicipioViewSet, MesaViewSet
from . import views
from .views import ResultadosPorMunicipioAPIView

router = DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'municipios', MunicipioViewSet)
router.register(r'mesas', MesaViewSet)

urlpatterns = [
    path("", views.index, name="index"),

    path("api/", include(router.urls)),
path("api/resultados/municipio/<int:municipio_id>/", ResultadosPorMunicipioAPIView.as_view(), name="resultados_municipio"),
]