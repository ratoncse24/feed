from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('/boards', views.home, name='home'),
    url('/boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url('/boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url('/boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url('/boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),


]
