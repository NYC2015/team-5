from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^dddddd$', views.createUser, name='Registration'),
  url(r'^$', views.home, name='Home'),

]
