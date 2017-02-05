from django.conf.urls import url
from.views import (
    posts_list,
    posts_create,
    posts_detail,
    posts_update,
    posts_delete
)

urlpatterns = [
    url(r'^create/$', posts_create),
    url(r'^(?P<slug>[\w-]+)/$', posts_detail, name='post_detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', posts_update, name='post_update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', posts_delete),
    url(r'^$', posts_list, name="list"),
]
