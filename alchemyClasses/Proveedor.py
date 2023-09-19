from alchemyClasses import db
from sqlalchemy import Column, Integer, String

class Proveedor(db.Model):

    __tablename__ = 'proveedores'
    id = Column(Integer, primary_key = True)
    empresa = Column(String(50))
    nombreContacto = Column(String(50))
    direccion = Column(String(50))
    ciudad = Column(String(25))
    estado = Column(String(25))
    codigoPostal = Column(String(10))
    email = Column(String(255))

    def __init__(self, empresa, nombreContacto, direccion, ciudad, estado, codigoPostal, email):
        self.empresa = empresa
        self.nombreContacto = nombreContacto
        self.direccion = direccion
        self.ciudad = ciudad
        self.estado = estado
        self.codigoPostal = codigoPostal
        self.email = email
    
    def __str__(self):
        return f'idProveedor: {self.id}, Empresa: {self.empresa}, Email: {self.email}'