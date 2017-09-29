from django.conf.urls import patterns, include, url
from django.contrib import admin
from siscaf import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^professor/', include('professor.urls')),
    url(r'^aluno/', include('aluno.urls')),
    url(r'^turma/', include('turma.urls')),
    url(r'^$', 'siscaf.views.index'),
    
    

)
