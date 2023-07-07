from app import app,db,ma

class Reserva(db.Model):   # la clase reserva hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    fecha=db.Column(db.Date)
    hora=db.Column(db.Time)
    telefono=db.Column(db.String(100))
    def __init__(self,nombre,fecha,hora,telefono):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.fecha=fecha
        self.hora=hora
        self.telefono=telefono
    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class ReservaSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','fecha','hora','telefono')

