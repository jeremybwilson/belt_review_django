from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^initialize$', views.initialize, name="initialize"),
    url(r'^books$', views.book, name="books"),
    url(r'^add$', views.add, name="add"),
    url(r'^(?P<book_id>\d+)$', views.showbook, name="showbook"),
    url(r'^addbookreviewprocess$', views.addbookreviewprocess, name="addbookreviewprocess"),
    url(r'^addreviewprocess/(?P<book_id>\d+)$', views.addreviewprocess, name="addreviewprocess"),
    url(r'^deletereview/(?P<review_id>\d+)$', views.deletereview, name="deletereview"),
]