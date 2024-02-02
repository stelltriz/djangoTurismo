from rest_framework.viewsets import ModelViewSet
from projetoturismo.models import PontoTuristico


class AccountViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer