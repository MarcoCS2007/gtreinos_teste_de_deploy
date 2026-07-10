from django.shortcuts import get_object_or_404, render, redirect
from django.http.response import HttpResponseForbidden
from .forms import ExercicioProfessorForm, ExercicioAlunoForm
from django.contrib.auth.decorators import login_required
from .models import Exercicio

# Create your views here.
@login_required
def criar_exercicio(request):
    if not hasattr(request.user, 'professor'):
        return HttpResponseForbidden("<h1>Acesso Negado. Apenas professores podem criar treinos.</h1>")

    if request.method == 'POST':
        form = ExercicioProfessorForm(request.POST)
        if form.is_valid():
            exercicio = form.save(commit=False)
            exercicio.professor = request.user.professor
            exercicio.save()

            return redirect('exercicios:lista')

    else:
        form = ExercicioProfessorForm()

    return render(request,'exercicios/criar.html', {'form': form})

@login_required
def visualizar_exercicio(request, exercicio_id):

    exercicio = get_object_or_404(Exercicio, id=exercicio_id)


    if hasattr(request.user, 'professor'):
        if exercicio.professor != request.user.professor:
            return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")

        return render(request, 'exercicios/visualizar_exercicio_professor.html', {'exercicio': exercicio})
    
    elif hasattr(request.user, 'aluno'):
        if exercicio.aluno != request.user.aluno:
            return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")

        if request.method == 'POST':
            form = ExercicioAlunoForm(request.POST, instance=exercicio)
            if form.is_valid():
                form.save()
                return redirect ('exercicios:lista')
        else:
            form = ExercicioAlunoForm(instance = exercicio)

        return render(request, 'exercicios/visualizar_exercicio_aluno.html', {'form': form})

    else:
        return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")

@login_required
def lista_exercicios(request):
    if hasattr(request.user, 'professor'):
        exercicios = Exercicio.objects.filter(professor=request.user.professor).order_by('-data_criacao')

    elif hasattr(request.user, 'aluno'):
        exercicios = Exercicio.objects.filter(aluno=request.user.aluno).order_by('-data_criacao')

    else:
        return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")

    return render(request, 'exercicios/lista.html', {'exercicios': exercicios})

@login_required
def deletar_exercicio(request, exercicio_id):
    
    exercicio = get_object_or_404(Exercicio, id=exercicio_id)

    if hasattr(request.user, 'professor'):
        if exercicio.professor != request.user.professor:
            return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")
        
    else:
        return HttpResponseForbidden("<h1>Acesso Negado. Você não tem permissão para acessar essa área!</h1>")

    if request.method =='POST':
        exercicio.delete()
        return redirect('exercicios:lista')

    return render(request, 'exercicios/deletar_exercicio.html', {'exercicio': exercicio})
