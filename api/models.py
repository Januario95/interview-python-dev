from django.db import models

import json
from datetime import datetime


default = lambda date: date.isoformat() if isinstance(date, datetime) else obj


class MessageQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values('id', 'sender', 'message_content', 'date_sent'))
        return list_values #json.dumps(list_values, indent=4, default=default)


class MessageManager(models.Manager):
    def get_queryset(self):
        return MessageQuerySet(self.model, using=self._db)


class UserModel(models.Model):
    name = models.CharField(max_length=100,
                            unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Chat User'
        verbose_name_plural = 'Chat Users'



class Message(models.Model):
    sender = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)
    message_content = models.CharField(max_length=1250)
    date_sent = models.DateTimeField(auto_now_add=True)

    objects = MessageManager()

    def __str__(self):
        return f'Sent by {self.sender.name} on {self.date_sent}'

    class Meta:
        ordering = ['date_sent']

