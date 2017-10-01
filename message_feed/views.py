from django.http.response import HttpResponseRedirect
from rest_framework import (
    generics,
    renderers,
    response,
    views,
)
from message_feed.models import Message
from message_feed.serializers.common_serializers import (
    MessageSerializer,
    MessageCommentSerializer,
)
from message_feed.paginators import MessagePaginator


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.filter(depth=0)
    pagination_class = MessagePaginator
    serializer_class = MessageSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        return response.Response(
            {'context': self.paginate_queryset(queryset=self.get_queryset())},
            content_type='text/html',
            template_name='pages/main_page.html',
        )


class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCommentSerializer
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    template_name = 'pages/single_message_page.html'


class CreateMessageView(views.APIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        return response.Response({}, template_name='pages/add_message_page.html')

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data.get('parent'):
                # Return rendered template for JS append.
                return response.Response(serializer.data, template_name='message_feed/message_comment.html')
            else:
                return HttpResponseRedirect(request.data.get('previous_page', '/'))
        else:
            return response.Response(
                {'errors': serializer.error_messages},
                template_name='pages/add_message_page.html',
            )