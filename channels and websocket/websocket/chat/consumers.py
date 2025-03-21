from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync 

class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # this extracts the room_name from the ws url!!
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username
            }
        )

    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        print(username)
        await self.send(json.dumps({'type':'group_chat','message':message,'username':username}))
