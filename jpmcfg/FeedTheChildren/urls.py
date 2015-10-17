from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^createUser$', views.createUser, name='Registration'),
  url(r'^$', views.home, name='Home'),
  url(r'^login$', views.loginUser, name="Login"),
]
