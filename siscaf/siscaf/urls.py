from django.conf.urls import patterns, include, url
from django.contrib import admin
from academico import views


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^professor/', include('Professor.urls')),
    url(r'^academico/', include('academico.urls')),
    url(r'^$', 'academico.views.index'),
    
    

)

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', include('Professor.urls')),
#     url(r'^$', 'academico.views.index'),
    

# ]