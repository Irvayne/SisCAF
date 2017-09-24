from django.conf.urls import patterns, include, url
from turma import views
from turma.views import RegistrarTurmaView

urlpatterns = patterns('',
   
    url(r'^listar$', views.listar, name='listar_turmas'),
   	url(r'^cadastrar$', RegistrarTurmaView.as_view(), name="cadastrar_turma"),
)