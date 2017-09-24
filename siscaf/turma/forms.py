from django import forms
from turma.models import Turma




class RegistrarTurmaForm(forms.Form):
    nome = forms.CharField(required=True)


    def is_valid(self):
        valid = True
        if not super(RegistrarTurmaForm, self).is_valid():
            self.adiciona_erro('Por favor, verifique os dados informados!')
            valid = False

        user_exists = Turma.objects.filter(nome=self.data['nome']).exists()

        if user_exists:
            self.adiciona_erro('Turma ja existente')
            valid = False
        return valid

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)





