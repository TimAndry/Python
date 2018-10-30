from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^wall$', views.wall),
    url(r'^message$', views.message),
    url(r'^comment$', views.comment),
    url(r'^delete$', views.delete),
    url(r'^logout$', views.logout),
    url(r'^tables$', views.tables),
]