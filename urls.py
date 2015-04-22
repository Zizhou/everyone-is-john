from django.conf.urls import patterns, url

from john import views

urlpatterns = patterns('',
    url(r'^$', views.main_page, name = 'main'),
    url(r'^post/(?P<post_id>\d+)/$', views.post, name = 'post'),
    url(r'^thread/(?P<thread_id>\d+)/$', views.ThreadView.as_view(), name = 'thread'),

)
