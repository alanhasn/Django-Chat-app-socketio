from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('chat/<str:room_name>/', views.chat_view, name='chat'),
]