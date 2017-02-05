from django.conf.urls import url
from.views import (
    UserCreateAPIView
)

urlpatterns = [
    # url(r'^$', CommentListViewAPIView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<pk>\d+)/edit/$', CommentEditAPIView.as_view(), name='edit'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
