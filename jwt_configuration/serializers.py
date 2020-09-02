#Criando uma nova serialização para o acesso do token jwt, excluindo o refresh e mantendo somente o token de acesso.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ObtainTokenAcessSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        del data['refresh']

        return data