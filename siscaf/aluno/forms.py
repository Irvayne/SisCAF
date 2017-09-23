from django import forms
from aluno.models import Aluno




class RegistrarAlunoForm(forms.Form):
    nome = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    rg = forms.CharField(required=True)
    sexo = forms.CharField(required=True)
    curso = forms.CharField(required=True)
    endereco = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    celular = forms.CharField(required=True)
    telefoneFixo = forms.CharField(required=True)
    password = forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(RegistrarAlunoForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados!')
            valid = False

        user_exists = Aluno.objects.filter(nome=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Usuario ja existente')
            valid = False
        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)





