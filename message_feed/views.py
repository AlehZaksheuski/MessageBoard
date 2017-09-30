from django.http.response import HttpResponseRedirect
from rest_framework import (
    generics,
    renderers,
    response,
    views,
    permissions,
)
from message_feed.models import Message
from message_feed.serializers.common_serializers import MessageCreateSerializer, MessageSerializer, \
    MessageCommentSerializer
from message_feed.paginators import MessagePaginator


class MainPageView(views.APIView):
    renderer_classes = (renderers.TemplateHTMLRenderer, )

    def get(self, request, *args, **kwargs):
        return response.Response({'context': Message.objects.filter(depth=0)[0:20]}, template_name='pages/main_page.html')


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
    renderer_classes = (renderers.TemplateHTMLRenderer, )
    serializer_class = MessageCommentSerializer
    queryset = Message.objects.all()

    def get(self, request, *args, **kwargs):
        parent_id = kwargs.get('pk')
        message = Message.objects.filter(id=parent_id).prefetch_related('message_set').first()

        if message.message_set.exists():
            page = request.query_params.get('page')
            count = message.message_set.all().count()
            if page and int(page) < count:
                message = message.message_set.all()[int(page)]

        return response.Response(
            {'message': self.serializer_class(instance=message).data},
            template_name='pages/single_message_page.html'
        )


class CreateMessageView(views.APIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer, )
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        return response.Response({}, template_name='pages/add_message_page.html')

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            new_message = serializer.save()
            if request.data.get('parent'):
                return response.Response({'comment': new_message}, template_name='message_feed/message_comment.html')
            else:
                return HttpResponseRedirect("/")
        else:
            return response.Response({'errors': serializer.error_messages}, template_name='pages/add_message_page.html')