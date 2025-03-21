from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync 

class AsyncChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat_room'

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
        await self.send(json.dumps({'message':'Hello Connected'}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,self.channel_name
        )
        print("WebSocket disconnected")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    async def chat_message(self,event):
        print(event)
        message = event['message']
        await self.send(json.dumps({'type':'chat','message':message}))
