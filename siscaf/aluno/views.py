from django.shortcuts import render, redirect
from aluno.models import Aluno
from aluno.forms import RegistrarAlunoForm
from django.views.generic.base import View


class RegistrarAlunoView(View):
    template_name = 'cadastrar_aluno.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # preenche o from
        form = RegistrarAlunoForm(request.POST)

        # verifica se eh valido
        if form.is_valid():
            dados_form = form.data


            # cria o perfil
            aluno = Aluno(nome=dados_form['nome'],
                            cpf=dados_form['cpf'],
                            rg=dados_form['rg'],
                            sexo=dados_form['sexo'],
                            curso=dados_form['curso'],
                            endereco=dados_form['endereco'],
                            email=dados_form['email'],
                            celular=dados_form['celular'],
                            telefoneFixo=dados_form['telefoneFixo'],
                            password=dados_form['password'],
                            )

            # grava no banco
            aluno.save()

            # redireciona para index
            return redirect('listar_aluno')

        # so chega aqui se nao for valido
        # vamos devolver o form para mostrar o formulario preenchido
        return render(request, self.template_name, {'form' : form})

def cadastrar_aluno(request):
	return render(request ,'cadastrar_aluno')

def listar_aluno(request):
	alunos = Aluno.objects.all()
	return render(request, 'listar_aluno.html',{'alunos':alunos})

def deletar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    aluno.delete()
    return redirect('listar_aluno')

def editar_aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request,'editar_aluno.html',{'aluno': aluno})






# Create your views here.
