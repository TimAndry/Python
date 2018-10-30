from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^quote$', views.quote),
    url(r'^q2uote$', views.q2uote),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^update/(?P<user_id>\d+)$', views.update),
    url(r'^delete$', views.delete),
    url(r'^del2ete$', views.del2ete),
    url(r'^logout$', views.logout),
    url(r'^full$', views.full),
    url(r'^added/(?P<quote_quoter_id>\d+)$', views.added),
    url(r'^like$', views.like),
    url(r'^error$', views.error),
]