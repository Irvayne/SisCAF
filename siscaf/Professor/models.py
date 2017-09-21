from django.db import models

# Create your models here.

class Professor(models.Model):
	nome = models.CharField(max_length=255,null=False)
	telefone = models.CharField(max_length=15,null=False)
	endereco = models.CharField(max_length=255,null=False)
	email = models.EmailField(max_length=255,null=False)
	cpf = models.CharField(max_length=15,null=False)
	rg = models.CharField(max_length=15,null=False)
	password = models.CharField(max_length=255,null=False)
