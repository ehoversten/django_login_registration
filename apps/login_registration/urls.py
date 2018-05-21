from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/process_reg$', views.process_reg),
    # url(r'^process_reg$', views.process_reg),
    url(r'^users/process_login$', views.process_login),
    # url(r'^process_login$', views.process_login),
    url(r'^success$', views.success),
]
