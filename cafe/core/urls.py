from django.conf.urls import patterns, include, url

urlpatterns = patterns('cafe.core.views',
                       url(r'^$', 'home', name='home'),
)
