from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.createuser, name='Registration')
  url(r'^$', views.login, name='Home')
]
