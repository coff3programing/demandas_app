from rest_framework import viewsets
from .serializer import DenunciaSerializer, DemandadoSerializer
from .models import Denuncia, Demandado
# Create your views here.


class DenunciaView(viewsets.ModelViewSet):
    serializer_class = DenunciaSerializer
    queryset = Denuncia.objects.all()


class DenunciadoView(viewsets.ModelViewSet):
    serializer_class = DemandadoSerializer
    queryset = Demandado.objects.all()
