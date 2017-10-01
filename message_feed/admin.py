from django.contrib import admin
from message_feed.models import Message
from message_feed.constants.admin import (
    MESSAGE_ADMIN_LIST_DISPLAY,
    MESSAGE_ADMIN_FIELDS,
    MESSAGE_ADMIN_READONLY_FIELDS
)

class MessageAdmin(admin.ModelAdmin):
    fields = MESSAGE_ADMIN_FIELDS
    readonly_fields = MESSAGE_ADMIN_READONLY_FIELDS
    list_display = MESSAGE_ADMIN_LIST_DISPLAY
    model = Message

admin.site.register(Message, MessageAdmin)