from django.urls import path
from chat import views

urlpatterns = [
    path('chats/', views.chats_api),
    path('chats/<int:chat_id>/', views.get_chat_details_api)
]
