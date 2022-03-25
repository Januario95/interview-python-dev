from django.contrib import admin

from .models import (
    UserModel, Message
)

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    date_hierarchy = 'created_at'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'sender', 'message_content', 'date_sent']
    search_fields = ['user']
    date_hierarchy = 'date_sent'

