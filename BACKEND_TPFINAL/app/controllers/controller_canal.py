from ..models.model_canal import ModeloCanal
from flask import request, session
from ..database import DatabaseConnection

class CanalController:
    
    @classmethod
    def get_canal(cls,canal_id):
        canal = ModeloCanal(canal_id=canal_id)
        result = ModeloCanal.get_canal(canal)
        if result is not None:
            return result.serialize(),200
        
    @classmethod  
    def get_all(cls):
        canal_objects= ModeloCanal.get_all()
        canales =[]
        for usuario in canal_objects:
            canales.append(usuario)
        return canales, 200
    