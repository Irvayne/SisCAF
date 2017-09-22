from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=255,null=False)
	cpf = models.CharField(max_length=15,null=False)
	rg = models.CharField(max_length=15,null=False)
	sexo = models.CharField(max_length=15,null=False)
	curso = models.CharField(max_length=15,null=False)
	endereco = models.CharField(max_length=255,null=False)
	email = models.EmailField(max_length=255,null=False)
	celular = models.CharField(max_length=15,null=False)
	telefoneFixo = models.CharField(max_length=15,null=False)
	password = models.CharField(max_length=255,null=False)
