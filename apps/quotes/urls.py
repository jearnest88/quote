from django.conf.urls import url
from . import views # This line is new!
urlpatterns = [
url(r'^quotes$', views.index),
url(r'^register_quote$', views.register_quote),
url(r'^quotes/favorite/(?P<id>\d+)$', views.favorite),
url(r'^quotes/destroy/(?P<id>\d+)$', views.destroy),
url(r'^quotes/user/(?P<id>\d+)$', views.userpage)
]
