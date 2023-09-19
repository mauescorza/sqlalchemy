from alchemyClasses import db
from sqlalchemy import Column, Integer, String

class Cliente(db.Model):

    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    domicilio = Column(String(50))
    ciudad = Column(String(25))
    estado = Column(String(25))
    codigoPostal = Column(String(10))
    email = Column(String(25))

    def __init__(self, nombre, domicilio, ciudad, estado, codigoPostal, email):
        self.nombre = nombre
        self.domicilio = domicilio
        self.ciudad = ciudad
        self.estado = estado
        self.codigoPostal = codigoPostal
        self.email = email
    
    def __str__(self):
        return f'idCliente: {self.id}, Nombre: {self.nombre}, Email: {self.email}'