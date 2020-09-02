from rest_framework import serializers
from django.contrib.auth.models import User


#Criando um seriliazer para o registro de um novo usuário no banco padrão User do Django.
#Para se criar um novo usuário so é necessário o registro de username e password.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user