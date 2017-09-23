from django.conf.urls import patterns, include, url
from aluno import views
from aluno.views import RegistrarAlunoView



urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'academico.views.index'),
   
    url(r'^cadastrar_aluno$', views.cadastrar_aluno, name='cadastrar_aluno'),
    url(r'^listar_aluno$', views.listar_aluno, name='listar_aluno'),
    url(r'^cadastrar_aluno/$', RegistrarAlunoView.as_view(), name="cadastrar_aluno"),
    url(r'^(?P<aluno_id>\d+)/deletar_aluno$', views.deletar_aluno, name='deletar_aluno'),
    url(r'^(?P<aluno_id>\d+)/editar_aluno$', views.editar_aluno, name='editar_aluno'),
    
     

)


# urlpatterns = [
#     #url(r'^admin/', include(admin.site.urls)),
#     #url(r'^$', 'academico.views.index'),
#     url(r'^$', views.index , name='index'),
#     url(r'^teste^$', views.teste , name='teste'),
     
# ]
