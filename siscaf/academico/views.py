from django.shortcuts import render, redirect
from django.http import HttpResponse
from Professor.models import Professor
from django.views.generic.base import View
from academico.forms import RegistrarProfessorForm


class RegistrarProfessorView(View):
    def post(self, request):
        form = RegistrarProfessorForm(request.POST)
        if form.is_valid:
            print('formulario valido')
            dados_form = form.data
            professor = Professor(nome=dados_form['nome'],
                                  telefone=dados_form['telefone'],
                                  endereco=dados_form['endereco'],
                                  cpf=dados_form['cpf'],
                                  rg=dados_form['rg'],
                                  email=dados_form['email'],
                                  password=dados_form['password'],
                                  )
            professor.save()
            return redirect('index')
        else:
            print('formulario nao valido')
            return redirect('cadastrar_professor')


def index(request):
    return render(request, "home.html")


def cadatrar_professor(request):
    return render(request, 'cadastrar.html')


def listar_professores(request):
    professores = Professor.objects.all()
    return render(request, 'listar_professores.html', {'professores': professores})
