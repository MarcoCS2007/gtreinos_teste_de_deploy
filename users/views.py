from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Professor, Aluno
from .forms import ProfessorForm, AlunoForm

# Create your views here.
@login_required
def home(request):
    if not (hasattr(request.user, 'aluno') or hasattr(request.user, 'professor')):
        return redirect('users:escolher_perfil')
    return redirect('core:home')

@login_required
def escolher_perfil(request):
    if hasattr(request.user, 'aluno') or hasattr(request.user, 'professor'):
        return redirect('users:home')
    return HttpResponse("""
        <h1>Você é Aluno ou Professor?</h1>
        <a href='/cadastro/aluno/'><button>Sou Aluno</button></a>
        <a href='/cadastro/professor/'><button>Sou Professor</button></a>
    """)

@login_required
def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            perfil_aluno = form.save(commit=False)
            perfil_aluno.user = request.user
            perfil_aluno.save()
        
            return redirect('users:home')
    
    else:
        form = AlunoForm()
        return render(request, 'users/cadastro_aluno.html', {'form': form})

@login_required
def cadastro_professor(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)

        if form.is_valid():
            perfil_professor = form.save(commit=False)
            perfil_professor.user = request.user
            perfil_professor.save()

            return redirect('users:home')

    else:
        form = ProfessorForm()
        return render(request, 'users/cadastro_professor.html', {'form': form})