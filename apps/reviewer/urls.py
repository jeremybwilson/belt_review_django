from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^register$', views.register, name="register"),
    url(r'^books$', views.books, name="books"),
    url(r'^add$', views.addbooks, name="add"),
    url(r'^users$', views.showuser, name="users"),
    url(r'^users/(?P<user_id>\d+)$$', views.showuser, name="showuser"),
    url(r'^books/(?P<book_id>\d+)$', views.showbook, name="showbook"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name="logout"),
]