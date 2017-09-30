from django.conf.urls import url, include
from django.contrib import admin
from message_feed.views import MainPageView


urlpatterns = [
    url(r'^$', MainPageView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^message_feed/', include('message_feed.urls', namespace='message_feed'))
]
