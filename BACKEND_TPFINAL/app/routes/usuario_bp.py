from flask import Blueprint

from ..controllers.controller_usuario import UsuarioController

usuario_bp = Blueprint ('usuario_bp',__name__)

usuario_bp.route('/login', methods = ['GET','POST'])(UsuarioController.login)
usuario_bp.route('/profile',methods = ['GET'])(UsuarioController.show_profile)
usuario_bp.route('/logout', methods = ['GET'])(UsuarioController.logout)
usuario_bp.route('/<int:usuario_id>', methods= ['GET'])(UsuarioController.get_usuario)
usuario_bp.route('/', methods=['GET'])(UsuarioController.get_all)
usuario_bp.route('/<int:usuario_id>', methods=['DELETE'])(UsuarioController.delete)