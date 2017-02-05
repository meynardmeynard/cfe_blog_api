from django.conf.urls import url
from.views import (
    CommentListViewAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,
    CommentEditAPIView
)

urlpatterns = [
    url(r'^$', CommentListViewAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name='edit'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
]
