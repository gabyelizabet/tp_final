from ..models.model_chat import ModeloChat
from flask import request, session
from ..database import DatabaseConnection

class ChatController:
    
    @classmethod
    def get_chat(cls,chat_id):
        chat = ModeloChat(chat_id=chat_id)
        result = ModeloChat.get_chat(chat)
        if result is not None:
            return result.serialize(),200
        
    @classmethod  
    def get_all(cls):
        chat_objects= ModeloChat.get_all()
        chats =[]
        for usuario in chat_objects:
            chats.append(usuario)
        return chats, 200