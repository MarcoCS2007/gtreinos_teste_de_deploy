from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cref = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.user.username

class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    peso = models.FloatField(null=False, blank=False)
    altura = models.FloatField(null=False, blank=False)
    idade = models.IntegerField(null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ('N', 'Null')], null=False, blank=False)
    
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name='alunos')

    def __str__(self):
        return self.user.username