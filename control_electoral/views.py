from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Departamento, Municipio, Mesa
from .serializers import DepartamentoSerializer, MunicipioSerializer, MesaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum

from .models import Mesa

# Create your views here.


def index(request):
    return HttpResponse("Proyecto Final - Modulo 5")


class DepartamentoViewSet(ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class MunicipioViewSet(ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class MesaViewSet(ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer


class ResultadosPorMunicipioAPIView(APIView):

    def get(self, request, municipio_id):

        mesas = Mesa.objects.filter(
            recinto__circunscripcion__asiento__municipio_id=municipio_id
        )

        resultados = mesas.aggregate(
            total_candidato1=Sum('candidato1'),
            total_candidato2=Sum('candidato2'),
            total_candidato3=Sum('candidato3'),
            total_candidato4=Sum('candidato4'),
            total_candidato5=Sum('candidato5'),
            total_emitidos=Sum('votos_emitidos'),
        )

        return Response(resultados)