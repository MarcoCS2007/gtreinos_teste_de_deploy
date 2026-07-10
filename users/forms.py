from django import forms
from .models import Aluno, Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        exclude = ['user']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ['user']