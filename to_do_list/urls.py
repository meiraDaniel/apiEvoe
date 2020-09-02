from django.urls import include, path
from rest_framework import routers
from to_do_list import views as to_do_list_views

router = routers.DefaultRouter()
router.register(r'activities', to_do_list_views.ToDoList)


urlpatterns = [
    path('', include(router.urls)),
]