from django.contrib import admin

from chat.models import Chat, ChatQuestion

# Register your models here.
admin.site.register(Chat)
admin.site.register(ChatQuestion)
