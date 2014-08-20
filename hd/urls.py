from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin




from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^welcome$', 'jobs.views.welcome', name='welcome'),
     url(r'^timeline$', 'jobs.views.timeline', name='timeline'),
     url(r'^profile/(?P<first_name>[\w\-/w]+)/', 'profiles.views.profile', name='profile'),
     url(r'^area/(?P<nombre>[\w\-/w]+)/', 'areas.views.area', name='area'),
     url(r'^empresa/(?P<usuario>[\w\-/w]+)/', 'jobs.views.empresa', name='empresa'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^add/$', 'jobs.views.add', name='add'),

     url(r'^$', 'home.views.home', name='home'),
    url(r'^login/$', 'home.views.enter', name='enter'),
    url(r'^log-out/$', 'home.views.log_out', name='log-out'),
    url('', include('social.apps.django_app.urls', namespace='social')),



    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),



    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
   


   
      


)


