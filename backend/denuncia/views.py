from rest_framework import viewsets
from .serializer import DenunciaSerializer
from .models import Denuncia
# Create your views here.
class DenunciaView(viewsets.ModelViewSet):
    serializer_class = DenunciaSerializer
    queryset = Denuncia.objects.all()