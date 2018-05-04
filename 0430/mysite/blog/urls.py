from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^new_post', views.new_post, name='new_post'),
    url(r'^post/(?P<id>[0-9]+)$', views.edit_post, name='edit_post'),
]