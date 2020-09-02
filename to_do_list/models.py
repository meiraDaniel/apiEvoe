from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Modelo para a todo list utilizando 4 campos, sendo que somente activity e description são necessários para se criar um novo modelo.
#A data possui um tempo default e o creator é criado automaticamente pelo usuário que está autenticado naquele momento.
class ToDo(models.Model):
    activity = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.activity