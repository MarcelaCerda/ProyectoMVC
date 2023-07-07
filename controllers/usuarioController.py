from app import app,ma
from models.usuariosModel import *
from flask import request, jsonify

usuario_schema=UsuarioSchema()            # El objeto producto_schema es para traer un user
usuarios_schema=UsuarioSchema(many=True)  # El objeto productos_schema es para traer multiples registros de user

# crea los endpoint o rutas (json)
@app.route('/usuarios',methods=['GET'])
def get_Usuarios():
    all_usuarios=Usuario.query.all()         # el metodo query.all() lo hereda de db.Model
    result=usuarios_schema.dump(all_usuarios)  # el metodo dump() lo hereda de ma.schema y                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/usuarios/<id>',methods=['GET'])
def get_usuario(id):
    usuario=Usuario.query.get(id)
    return usuario_schema.jsonify(usuario)   # retorna el JSON de un user recibido como parametro

@app.route('/usuarios/<id>',methods=['DELETE'])
def delete_usuario(id):
    usuario=Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return usuario_schema.jsonify(usuario)   # me devuelve un json con el registro eliminado


@app.route('/usuarios', methods=['POST']) # crea ruta o endpoint
def create_usuario():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    apellido=request.json['apellido']
    email=request.json['email']
    clave=request.json['clave']
    dni=request.json['dni']
    telefono=request.json['telefono']

    new_usuario=Usuario(nombre,apellido,email,clave,dni,telefono)
    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.jsonify(new_usuario)


@app.route('/usuarios/<id>' ,methods=['PUT'])
def update_usuario(id):
    usuario=Usuario.query.get(id)
 
    usuario.nombre=request.json['nombre']
    usuario.apellido=request.json['apellido']
    usuario.email=request.json['email']
    usuario.clave=request.json['clave']
    usuario.dni=request.json['dni']
    usuario.telefono=request.json['telefono']

    db.session.commit()
    return usuario_schema.jsonify(usuario)



