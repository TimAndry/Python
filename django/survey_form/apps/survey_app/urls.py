from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^page$', views.page),
    url(r'^results$', views.results),
]