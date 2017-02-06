from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^cargarrestaurantes/$', views.cargarrestaurantes),
  url(r'^addRestaurantes/$', views.addRestaurantes, name="addRestaurantes"),
  url(r'^eliminar/$', views.eliminar, name="eliminar"),
   url(r'^actualiza/$', views.actualiza, name="actualiza"),

]
