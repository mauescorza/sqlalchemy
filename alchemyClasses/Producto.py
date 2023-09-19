from alchemyClasses import db
from sqlalchemy import Column, Integer, String, Numeric

class Producto(db.Model):

    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    descripcion = Column(String(100))
    precio = Column(Numeric(10,2))
    marca = Column(String(25))
    existencia = Column(Integer)

    def __init__(self, descripcion, precio, marca, existencia):
        self.descripcion = descripcion
        self.precio = precio
        self.marca = marca
        self.existencia = existencia
    
    def __str__(self):
        return f'idProducto: {self.id}, Descripcion: {self.descripcion}, Marca: {self.marca}, Precio: {self.precio}'