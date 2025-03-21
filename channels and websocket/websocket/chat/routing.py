from django.urls import re_path
from chat.consumers import AsyncChatConsumer

websocket_urlpatterns = [
    # Here regular expression is used instead of <str:room_name> because re_path doesn't support it
    re_path(r'ws/chat/(?P<room_name>\w+)/$', AsyncChatConsumer.as_asgi()),  # WebSocket route
]
