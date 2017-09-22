from django.shortcuts import render
from aluno.models import Aluno

def cadastrar_aluno(request):
	return render(request ,'cadastrar_aluno.html')

def listar_aluno(request):
	alunos = Aluno.objects.all()
	return render(request, 'listar_aluno.html',{'alunos':alunos})	

# Create your views here.
