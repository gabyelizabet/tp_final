from ..database import DatabaseConnection

class ModeloUsuario:
    
    def __init__(self, usuario_id= None, nombre_usuario= None, nombre = None, apellido= None, email= None, contraseña= None, f_nacim= None, foto= None):
            self.usuario_id = usuario_id
            self.nombre_usuario = nombre_usuario
            self.nombre = nombre
            self.apellido = apellido
            self.email = email
            self.contraseña = contraseña
            self.f_nacim = f_nacim
            self.foto= foto
            
            
    def serialize(self):
            return{
                "usuario_id" : self.usuario_id,
                "nombre_usuario" : self.nombre_usuario,
                "nombre" : self.nombre,
                "apellido" : self.apellido,
                "email" : self.email,
                "contraseña" : self.contraseña,
                "f_nacim" : self.f_nacim,
                "foto": self.foto
                }
            
    @classmethod
    def is_registered(cls, usuarios):
        """Metodo que permite conocer si un usuario esta registrado"""
        query = "SELECT email FROM mensajero.usuarios WHERE email = %s and contraseña = %s;"
        params = (usuarios.email, usuarios.contraseña)
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return True
        return False
    
    @classmethod
    def get_usuario(cls, usuarios):
        query = """SELECT * FROM mensajero.usuarios WHERE usuario_id = %s"""
        params = usuarios.usuario_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        
        if result is not None:
            return cls(
                usuario_id = result[0],
                nombre_usuario = result[1],
                nombre = result [2],
                apellido = result[3],
                email = result[4],
                contraseña = result[5],
                f_nacim = result[6],
                foto = result [7]
            )
        return None
    
    @ classmethod
    def get_all(cls):
        query= """SELECT * FROM mensajero.usuarios"""
        results = DatabaseConnection.fetch_all(query)
        usuarios=[]
        if results is not None:
            for result in results:
                usuarios.append({
                    'usuario_id' : result[0],
                    'nombre_usuario' : result[1],
                    'nombre' : result [2],
                    'apellido' : result[3],
                    'email' : result[4],
                    'contraseña' : result[5],
                    'f_nacim' : result[6],
                    'foto' : result [7]
                    })
        return usuarios,200
    
    @classmethod
    def crear_usuario(cls, usuario):
        query= "INSERT INTO mensajero.usuarios (nombre_usuario, nombre, apellido, email, contraseña, f_nacim) VALUES (%s, %s, %s, %s, %s,%s)"
        params = (usuario.nombre_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.contraseña, usuario.f_nacim)
        DatabaseConnection.execute_query(query, params)
    
    @classmethod
    def delete (cls, usuario):
        query = "DELETE FROM mensajero.usuarios WHERE usuario_id = %s"
        params = usuario.usuario_id,
        DatabaseConnection.execute_query(query, params=params)