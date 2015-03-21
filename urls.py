from django.conf.urls import patterns, url

from john import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name = 'main'),
)
