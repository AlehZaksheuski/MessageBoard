from django.db import models


class TimestampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Message(TimestampModel):
    text = models.TextField(blank=True)
    parent = models.ForeignKey("message_feed.Message", blank=True, null=True)
    depth = models.IntegerField(default=0)

    @property
    def has_children(self):
        return Message.objects.filter(parent=self).exists()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created_on', 'id')