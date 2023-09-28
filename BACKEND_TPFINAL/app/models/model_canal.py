from ..database import DatabaseConnection

class ModeloCanal:
    
    def __init__(self, canal_id= None, nombre_canal= None, usuar_serv_id= None):
            self.canal_id = canal_id
            self.nombre_canal = nombre_canal
            self.usuar_serv_id = usuar_serv_id
    
    def serialize(self):
            return{
                "canal_id" : self.canal_id,
                "nombre_canal" : self.nombre_canal,
                "usuar_serv_id" : self.usuar_serv_id
                }

    @classmethod
    def get_canal(cls, canal):
        query = """SELECT * FROM mensajero.canales WHERE canal_id = %s"""
        params = canal.canal_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(
                canal_id = result[0],
                nombre_canal = result[1],
                usuar_serv_id = result [2],
            )
        return None
    
    @ classmethod
    def get_all(cls):
        query= """SELECT * FROM mensajero.canales"""
        results = DatabaseConnection.fetch_all(query)
        canales=[]
        if results is not None:
            for result in results:
                canales.append({
                    'canal_id' : result[0],
                    'nombre_canal' : result[1],
                    'usuar_serv_id' : result [2],
                    })
        return canales,200