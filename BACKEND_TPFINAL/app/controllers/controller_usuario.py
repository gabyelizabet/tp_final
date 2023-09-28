from ..models.model_usuario import ModeloUsuario
from flask import request, session



class UsuarioController:
    
    @classmethod
    def login(cls):
        data = request.json
        usuario= ModeloUsuario(
            email= data.get('email'),
            contraseña= data.get('contraseña')
        )
        if ModeloUsuario.is_registered(usuario):
            session['email'] = data.get('email')
            return{"mensaje":"Sesion iniciada"}, 200
        else:
            return{"mensaje":"Usuario o contraseña incorrectos"}, 401
   
    @classmethod
    def show_profile(cls):
        email= session.get('email')
        email = ModeloUsuario.get_usuario(ModeloUsuario(email= email)) 
        if email is None:
            return {"mensaje":"Usuario no encontrado"}, 404
        else:
            return ModeloUsuario.serialize(), 200   
        
    @classmethod
    def logout(cls):
        session.pop('email', None)
        return { "mensaje":"Sesión cerrada"}, 200
    
    
    @classmethod
    def get_usuario(cls,usuario_id):
        usuario = ModeloUsuario(usuario_id=usuario_id)
        result = ModeloUsuario.get_usuario(usuario)
        if result is not None:
            return result.serialize(),200
      
    @classmethod  
    def get_all(cls):
        usuarios_objects= ModeloUsuario.get_all()
        usuarios =[]
        for usuario in usuarios_objects:
            usuarios.append(usuario)
        return usuarios, 200
    
    @classmethod
    def crear_usuario(cls, usuario):
        if request.method == 'POST':
                nombre_usuario = request.data.get('nombre_usuario'),
                nombre = request.data.get('nombre'),
                apellido = request.data.get('apellido'),
                email = request.data.get('email'),
                contraseña = request.data.get('contraseña') ,
                f_nacim = request.data.get('f_nacim'),
                
                usuario= ModeloUsuario(nombre_usuario,nombre,apellido, email, contraseña,f_nacim)
                
                if nombre_usuario and nombre and apellido and email and contraseña and f_nacim is None:
                    return {'Se requiere que ingrese todos los datos'}
                
                email = ModeloUsuario.filter_by(email=email).first()
    
    @classmethod
    def delete(cls, usuario_id):
        usuario= ModeloUsuario(usuario_id = usuario_id)
        
        if usuario is not None:
            ModeloUsuario.delete(usuario)
            return  {'message': 'User deleted successfully'}, 204
        else:
            return  {'message': 'User the user does not exist'}           
    
    