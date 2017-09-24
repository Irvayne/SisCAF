from django.shortcuts import render, redirect
from professor.models import Professor
from professor.forms import RegistrarProfessorForm
from django.views.generic.base import View


def listar(request):
    professores = Professor.objects.all()
    return render(request, 'listar_professores.html', {'professores': professores})


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

