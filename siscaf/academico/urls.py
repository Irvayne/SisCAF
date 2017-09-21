from django.conf.urls import patterns, include, url
from django.contrib import admin
from academico import views
from academico.views import RegistrarProfessorView


urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'academico.views.index'),
    url(r'^$', views.index , name='index'),
    url(r'^cadastrar_professor$',views.cadatrar_professor ,name='cadastrar_professor'),
    url(r'^registrar/$',RegistrarProfessorView.as_view(), name="registrar"),
    url(r'^listar_professores$', views.listar_professores, name='listar_professores')
     

)


# urlpatterns = [
#     #url(r'^admin/', include(admin.site.urls)),
#     #url(r'^$', 'academico.views.index'),
#     url(r'^$', views.index , name='index'),
#     url(r'^teste^$', views.teste , name='teste'),
     
# ]

