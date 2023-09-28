from flask import Blueprint

from ..controllers.controller_servidor import ServidorController

servidor_bp = Blueprint ('servidor_bp',__name__)

servidor_bp.route('/<int:servidor_id>', methods= ['GET'])(ServidorController.get_servidor)
servidor_bp.route('/', methods=['GET'])(ServidorController.get_all)