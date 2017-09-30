from django.db import models

class Turma(models.Model):
	nome = models.CharField(max_length=255, null=False)
	curso = models.CharField(max_length=255, null=False)
