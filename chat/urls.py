from django.urls import path
from chat import views

urlpatterns = [
    path('chats/', views.get_all_chats_api)
]