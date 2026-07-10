from django.db import models

class Exercicio(models.Model):
    # Dados Base e Prescrição (Professor)
    nome = models.CharField(max_length=100)
    aluno = models.ForeignKey('users.Aluno', on_delete=models.CASCADE, related_name='exercicios')
    professor = models.ForeignKey('users.Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='exercicios_criados')
    
    # Datas
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_realizacao = models.DateTimeField(null=True, blank=True) # Quando o aluno deve fazer
    
    # Execução (Aluno preenche ou o professor já deixa pré-definido)
    series = models.IntegerField(null=True, blank=True) # <-- NOVO CAMPO
    repeticoes = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True) # Float é ótimo para cargas quebradas (ex: halteres de 12.5kg)
    
    # Status
    esta_concluido = models.BooleanField(default=False)

    def __str__(self):
        # Exemplo: "Supino Reto - João (Concluído: False)"
        return f"{self.nome} - {self.aluno.user.username} (Concluído: {self.esta_concluido})"