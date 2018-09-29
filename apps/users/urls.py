from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.register, name="register"),
    url(r'^(?P<user_id>\d+)$$', views.showuser, name="showuser"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]