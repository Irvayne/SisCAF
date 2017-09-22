from django.conf.urls import patterns, include, url
from aluno import views



urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'academico.views.index'),
   
    url(r'^cadastrar_aluno$', views.cadastrar_aluno, name='cadastrar_aluno'),
    url(r'^listar_aluno$', views.listar_aluno, name='listar_aluno')
    
     

)


# urlpatterns = [
#     #url(r'^admin/', include(admin.site.urls)),
#     #url(r'^$', 'academico.views.index'),
#     url(r'^$', views.index , name='index'),
#     url(r'^teste^$', views.teste , name='teste'),
     
# ]
