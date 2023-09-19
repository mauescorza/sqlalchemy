from alchemyClasses import db
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Numeric

class Pedido(db.Model):

    __tablename__ = 'pedidos'
    numeroPedido = Column(Integer, primary_key=True)
    vendedor = Column(String(50))
    fechaPedido = Column(Date)
    producto = Column(Integer, ForeignKey('productos.id'))
    cantidad = Column(Integer)
    precio = Column(Numeric(10,2))
    total = Column(Numeric(10,2))

    def __init__(self, vendedor, fechaPedido, producto, cantidad, precio):
        self.vendedor = vendedor
        self.fechaPedido = fechaPedido
        self.producto = producto
        self.cantidad = cantidad
        self.precio = precio
        self.total = round(self.cantidad * self.precio, 2)
    
    def __str__(self):
        return f'idPedido: {self.numeroPedido}, Fecha: {self.fechaPedido}, Total: {self.total}'