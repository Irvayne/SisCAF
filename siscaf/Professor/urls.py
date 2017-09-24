from django.conf.urls import patterns, include, url
from django.contrib import admin
from professor import views
from professor.views import RegistrarProfessorView


urlpatterns = patterns('',
  
  	url(r'^listar$', views.listar, name='listar_professores'),
   	url(r'^cadastrar$', RegistrarProfessorView.as_view(), name="cadastrar_professor"),
)