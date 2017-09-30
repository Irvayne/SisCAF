from django.shortcuts import render, redirect
from turma.models import Turma
from turma.forms import RegistrarTurmaForm
from django.views.generic.base import View
from aluno.models import Aluno


def listar(request):
	turmas = Turma.objects.all()
	return render(request, 'listar.html',{'turmas':turmas})

def deletar_turma(request, turma_id):
    turma = Turma.objects.get(id=turma_id)
    turma.delete()
    return redirect('listar_turmas')

class RegistrarTurmaView(View):
    template_name = 'cadastrar_turma.html'

    def get(self, request):
        alunos = Aluno.objects.all()
        return render(request, self.template_name, {'alunos':alunos})

    def post(self, request):
        # preenche o from
        form = RegistrarTurmaForm(request.POST)

        # verifica se eh valido
        if form.is_valid():
            dados_form = form.data


            # cria o perfil
            turma = Turma(nome=dados_form['nome'],curso=dados_form['curso'])

            # grava no banco
            turma.save()

            # redireciona para index
            return redirect('listar_turmas')

        # so chega aqui se nao for valido
        # vamos devolver o form para mostrar o formulario preenchido
        return render(request, self.template_name, {'form' : form})


