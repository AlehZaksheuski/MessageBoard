from django.conf.urls import url
from message_feed.views import (
    CreateMessageView,
    MessageListView,
    MessageRetrieveView,
)

urlpatterns = [
    url(r'^get_message/(?P<pk>[0-9]+)', MessageRetrieveView.as_view(), name='get_message_comment'),
    url(r'^get_message', MessageListView.as_view(), name='get_message'),
    url(r'^add_message', CreateMessageView.as_view(), name='add_message'),
]
