from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'jobs.views.home', name='home'),
      url(r'^profile/(?P<first_name>[\w\-/w]+)/', 'profiles.views.profile', name='profile'),
       url(r'^area/(?P<nombre>[\w\-/w]+)/', 'areas.views.area', name='area'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
