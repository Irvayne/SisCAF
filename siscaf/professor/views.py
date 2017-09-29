from django.shortcuts import render, redirect
from professor.models import Professor
from professor.forms import RegistrarProfessorForm
from django.views.generic.base import View


class RegistrarProfessorView(View):
    template_name = 'cadastrar_professor.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # preenche o from
        form = RegistrarProfessorForm(request.POST)

        # verifica se eh valido
        if form.is_valid():
            dados_form = form.data


            # cria o perfil
            professor = Professor(nome=dados_form['nome'],
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
            professor.save()

            # redireciona para index
            return redirect('listar_professor')

        # so chega aqui se nao for valido
        # vamos devolver o form para mostrar o formulario preenchido
        return render(request, self.template_name, {'form' : form})

def cadastrar_professor(request):
	return render(request ,'cadastrar_professor')

def listar_professor(request):
	professor = Professor.objects.all()
	return render(request, 'listar_professor.html',{'professor':professor})

def deletar_professor(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    professor.delete()
    return redirect('listar_professor')

def editar_professor(request, professor_id):
    professor = Professor.objects.get(id=professor_id)
    return render(request,'editar_professor.html',{'professor': professor})






# Create your views here.
