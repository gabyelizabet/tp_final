from ..database import DatabaseConnection


class ModeloChat:
    
    def __init__(self, chat_id= None,  canal_id=None,fecha=None, mensaje= None):
            self.chat_id = chat_id
            self.canal_id = canal_id
            self.fecha = fecha
            self.mensaje = mensaje
    
    def serialize(self):
            return{
                "chat_id" : self.chat_id,
                "canal_id" : self.canal_id,
                "fecha" : self.fecha,
                "mensaje": self.mensaje
                }
    
    @classmethod
    def get_chat(cls, chat):
        query = """SELECT * FROM mensajero.chats WHERE chat_id = %s"""
        params = chat.chat_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(
                chat_id = result[0],
                canal_id = result[1],
                fecha = result [2],
                mensaje = result[3]
            )
        return None
    
    @ classmethod
    def get_all(cls):
        query= """SELECT * FROM mensajero.chats"""
        results = DatabaseConnection.fetch_all(query)
        chats=[]
        if results is not None:
            for result in results:
                chats.append({
                    'chat_id' : result[0],
                    'canal_id' : result[1],
                    'fecha' : result [2],
                    'mensaje': result[3],
                    })
        return chats,200