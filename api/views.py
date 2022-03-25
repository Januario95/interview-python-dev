from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import (
    UserModel, Message
)
from .serializers import MessageSerializer

def fetch_all_messages(request):
    messages = Message.objects.all()

    return JsonResponse({
        'messages': messages.serialize()
    })


class MessageView(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


def create_user(request, username):
    user = UserModel.objects.filter(name=username)
    if user.exists():
        user = user.first()
    else:
        user = UserModel.objects.create(name=username)

    return JsonResponse({
        'username': user.name
    })


def create_message(request, username, message):
    user = UserModel.objects.filter(name=username)
    created = False
    if user.exists():
        user = user.first()
        message = Message.objects.create(
            sender=user,
            message_content=message
        )
        message.save()
        created = True
    else:
        pass

    return JsonResponse({
        'user_created': created
    })


