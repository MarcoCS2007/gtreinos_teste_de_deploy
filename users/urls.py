from django.urls import path, include
from .views import cadastro_aluno, cadastro_professor, home, escolher_perfil

app_name='users'

urlpatterns = [
    path('', home, name='home'),
    path('cadastro/escolha/', escolher_perfil, name='escolher_perfil'),
    path('cadastro/aluno/', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro/professor/', cadastro_professor, name='cadastro_professor'),
]