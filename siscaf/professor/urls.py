from django.conf.urls import patterns, include, url
from professor import views
from professor.views import RegistrarProfessorView



urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'academico.views.index'),
   
    url(r'^cadastrar_professor$', views.cadastrar_professor, name='cadastrar_professor'),
    url(r'^listar_professor$', views.listar_professor, name='listar_professor'),
    url(r'^cadastrar_professor/$', RegistrarProfessorView.as_view(), name="cadastrar_professor"),
    url(r'^(?P<professor_id>\d+)/deletar_professor$', views.deletar_professor, name='deletar_professor'),
    url(r'^(?P<professor_id>\d+)/editar_professor$', views.editar_professor, name='editar_professor'),
    
     

)


# urlpatterns = [
#     #url(r'^admin/', include(admin.site.urls)),
#     #url(r'^$', 'academico.views.index'),
#     url(r'^$', views.index , name='index'),
#     url(r'^teste^$', views.teste , name='teste'),
     
# ]
