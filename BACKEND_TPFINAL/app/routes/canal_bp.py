from flask import Blueprint

from ..controllers.controller_canal import CanalController

canal_bp = Blueprint ('canal_bp',__name__)

canal_bp.route('/<int:canal_id>', methods= ['GET'])(CanalController.get_canal)
canal_bp.route('/', methods=['GET'])(CanalController.get_all)