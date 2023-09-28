from ..models.model_servidor import ModeloServidor
from flask import request, session
from ..database import DatabaseConnection

class ServidorController:
    
    @classmethod
    def get_servidor(cls,servidor_id):
        servidor = ModeloServidor(servidor_id=servidor_id)
        result = ModeloServidor.get_serv(servidor)
        if result is not None:
            return result.serialize(),200
        
    @classmethod  
    def get_all(cls):
        servidor_objects= ModeloServidor.get_all()
        servidores =[]
        for usuario in servidor_objects:
            servidores.append(usuario)
        return servidores, 200
    