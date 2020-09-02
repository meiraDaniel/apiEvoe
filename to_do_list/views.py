from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from to_do_list.models import ToDo
from to_do_list.serializers import ToDoSerializer
from to_do_list.permissions import IsCreatorOrReadOnly

class ToDoList(viewsets.ModelViewSet) :
    #Permisões que limitam a visualização da API a usuários autenticados e a edição e exclusão aos criadores daquela atividade.
    permission_classes = (IsAuthenticated, IsCreatorOrReadOnly,)
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    #Metodo responsável por assim que uma nova atividade for criada automaticamente passa para o serializer do ToDoList quem é o usuário autenticado no momento. 
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)