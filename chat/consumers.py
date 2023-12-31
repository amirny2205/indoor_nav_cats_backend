from channels.consumer import AsyncConsumer
from .models import MessageModel
from django.contrib.auth import get_user_model
import json


User = get_user_model()


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        text = json.loads(text_data['text'])
        if 'msg_from' in text.keys():
            msg_from = await User.objects.\
                filter(username=text['msg_from']).afirst()
            msg_to = await User.objects.\
                filter(username=text['msg_to']).afirst()
            await MessageModel.objects.acreate(
                msg_from=msg_from,
                msg_to=msg_to,
                content=text['content'])
        await self.send({
            "type": "websocket.send",
            "text": "recieved a message from you"
        })

    async def websocket_disconnect(self, event):
        pass
