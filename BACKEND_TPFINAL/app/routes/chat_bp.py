from flask import Blueprint

from ..controllers.controller_chats import ChatController

chat_bp = Blueprint ('chat_bp',__name__)

chat_bp.route('/<int:chat_id>', methods= ['GET'])(ChatController.get_chat)
chat_bp.route('/', methods=['GET'])(ChatController.get_all)