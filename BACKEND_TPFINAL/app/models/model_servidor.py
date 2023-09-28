from ..database import DatabaseConnection

    
class ModeloServidor:
 
    def __init__(self, servidor_id=None, nombre_serv= None, icono=None):
            self.servidor_id = servidor_id
            self.nombre_serv = nombre_serv
            self.icono = icono
 
    def serialize(self):
            return{
                "servidor_id" : self.servidor_id,
                "nombre_servi" : self.nombre_serv,
                "icono" : self.icono
                }

    @classmethod
    def get_serv(cls, servidor):
        query = """SELECT * FROM mensajero.servidores WHERE servidor_id = %s """
        params = servidor.servidor_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(
                servidor_id = result[0],
                nombre_serv = result[1],
                icono = result [2]
            )
        return None
    
    @ classmethod
    def get_all(cls):
        query= """SELECT * FROM mensajero.servidores"""
        results = DatabaseConnection.fetch_all(query)
        servidores=[]
        if results is not None:
            for result in results:
                servidores.append({
                    'servidor_id' : result[0],
                    'nombre_serv' : result[1],
                    'icono' : result [2],
                    })
        return servidores,200
    
    @classmethod
    def delete(cls, usuario):
        query= "DELETE FROM mensajero.usuarios WHERE usuario_id = %s"
        params= usuario.usuario_id,
        DatabaseConnection.execute_query(query, params= params)