from app import app,ma
from models.reservaModel import *
from flask import request, jsonify

reserva_schema=ReservaSchema()            # El objeto reserva_schema es para traer un reserva
reservas_schema=ReservaSchema(many=True)  # El objeto reservas_schema es para traer multiples registros de reserva

# crea los endpoint o rutas (json)
@app.route('/reservas',methods=['GET'])
def get_Reservas():
    all_reservas=Reserva.query.all()         # el metodo query.all() lo hereda de db.Model
    result=reservas_schema.dump(all_reservas)  # el metodo dump() lo hereda de ma.schema y
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla

@app.route('/reservas/<id>',methods=['GET'])
def get_reserva(id):
    reserva=Reserva.query.get(id)
    return reserva_schema.jsonify(reserva)   # retorna el JSON de un reserva recibido como parametro

@app.route('/reservas/<id>',methods=['DELETE'])
def delete_reserva(id):
    reserva=Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return reserva_schema.jsonify(reserva)   # me devuelve un json con el registro eliminado

@app.route('/reservas', methods=['POST']) # crea ruta o endpoint
def create_reserva():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    fecha=request.json['fecha']
    hora=request.json['hora']
    telefono=request.json['telefono']
    new_reserva=Reserva(nombre,fecha,hora,telefono)
    db.session.add(new_reserva)
    db.session.commit()
    return reserva_schema.jsonify(new_reserva)

@app.route('/reservas/<id>' ,methods=['PUT'])
def update_reserva(id):
    reserva=Reserva.query.get(id)
    reserva.nombre=request.json['nombre']
    reserva.fecha=request.json['fecha']
    reserva.hora=request.json['hora']
    reserva.telefono=request.json['telefono']
    db.session.commit()
    return reserva_schema.jsonify(reserva)
 

