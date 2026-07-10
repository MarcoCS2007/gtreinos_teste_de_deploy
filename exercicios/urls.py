from django.urls import path
from .views import lista_exercicios, deletar_exercicio, criar_exercicio, visualizar_exercicio

app_name = 'exercicios'

urlpatterns = [
    path('', lista_exercicios, name='lista'),
    path('criar/', criar_exercicio, name='criar'),
    path('deletar/<int:exercicio_id>/', deletar_exercicio, name='deletar'),
    path('visualizar/<int:exercicio_id>/', visualizar_exercicio, name='visualizar')
]