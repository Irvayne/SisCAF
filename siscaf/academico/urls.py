from django.conf.urls import patterns, include, url
from django.contrib import admin
from academico import views



urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'academico.views.index'),
    url(r'^$', views.index , name='index'),
     

)
