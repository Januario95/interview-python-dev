from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    fetch_all_messages, MessageView,
    create_user, create_message
)

router = DefaultRouter()
router.register('messages', MessageView,
                basename='Message')

urlpatterns = [
    path('all_messages/', fetch_all_messages),
    path('create_user/<str:username>/', create_user),
    path('create_message/<str:username>/<str:message>/',
         create_message),
    path('', include(router.urls)),
]
