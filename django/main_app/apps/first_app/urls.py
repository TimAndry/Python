from django.conf.urls import url
#gives access to the function urls
from . import views
#imports views.py in the current folder

#interprets the regex and matches it as a string. the url is empty according to the regex so the route is '/'
urlpatterns = [
    url(r'^$', views.index)
]