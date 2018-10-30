from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^total$', views.total),
    url(r'^confirmation$', views.confirmation)

]
