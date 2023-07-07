from app import app,db,ma

class Usuario(db.Model):   # la clase reserva hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    apellido=db.Column(db.String(100))
    email=db.Column(db.String(100))
    clave=db.Column(db.String(100))
    dni=db.Column(db.Integer)
    telefono=db.Column(db.String(100))
    
    def __init__(self,nombre,apellido, email,clave,dni,telefono):   #crea el  constructor de la clase
        self.nombre=nombre
        self.apellido=apellido   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.email=email
        self.clave=clave        
        self.dni=dni
        self.telefono=telefono
    #  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class UsuarioSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','apellido','email','clave','dni','telefono' )
        

