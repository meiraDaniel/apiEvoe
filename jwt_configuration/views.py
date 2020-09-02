#Criando uma nova view para utilizar o novo serializer criado.

from rest_framework_simplejwt.views import TokenObtainPairView
from jwt_configuration.serializers import ObtainTokenAcessSerializer 

class ObtainTokenAcessView(TokenObtainPairView):
    serializer_class = ObtainTokenAcessSerializer