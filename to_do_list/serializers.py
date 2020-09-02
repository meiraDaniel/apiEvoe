from rest_framework import serializers
from to_do_list.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    #Inicializando o creator no serializer como um campo somente de leitura, e obtendo o valor do username do usuário autenticado no momento.
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = ToDo
        fields = '__all__'