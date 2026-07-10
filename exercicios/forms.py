from django import forms
from .models import Exercicio

class ExercicioProfessorForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['nome', 'aluno', 'data_realizacao', 'series', 'repeticoes']
        labels = {
            'nome': 'Nome do exercício',
            'aluno': 'Aluno',
            'data_realizacao': 'Data e hora do treino',
            'series': 'Séries',
            'repeticoes': 'Repetições',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Ex: Supino reto'}),
            'data_realizacao': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M',
            ),
            'series': forms.NumberInput(attrs={'min': 1, 'step': 1}),
            'repeticoes': forms.NumberInput(attrs={'min': 1, 'step': 1}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_realizacao'].input_formats = ['%Y-%m-%dT%H:%M']

class ExercicioAlunoForm(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['peso', 'esta_concluido']
        labels = {
            'peso': 'Carga do top set (kg)',
            'esta_concluido': 'Treino concluído',
        }
        widgets = {
            'peso': forms.NumberInput(attrs={'step': '0.5', 'min': '0'}),
        }