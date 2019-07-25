from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^add_user$', views.add_user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]