from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(?P<course_id>\d+)$', views.delete),
    url(r'^no$', views.no),
    url(r'^edit/(?P<course_id>\d+)$', views.edit),
]