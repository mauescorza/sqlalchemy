from alchemyClasses.Cliente import db
from flask import Flask
from alchemyClasses.Cliente import Cliente
from alchemyClasses.Pedido import Pedido
from alchemyClasses.Producto import Producto
from alchemyClasses.Proveedor import Proveedor
import random
from datetime import datetime
from sqlalchemy import and_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://mauescorza:Ejercicio2!@localhost:3306/ejercicio2"
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

menu = '\nSeleccione una opcion:\n1) Llenar 15 registros por cada tabla.\n2) Desplegar el resultado de 6 consultas.\n3) Actualizar 4 datos.\n4) Eliminar 5 datos.\n5) Salir'

if __name__ == '__main__':
    with app.app_context():
        choice = 1
        while choice != 5:
            print(menu)
            choice = int(input())

            if choice == 1:

                # Poblar clientes
                db.session.add(Cliente("Ernesto", "Calle Paz 61","Guanajuato", "Guanajuato", "CP204359", "ernesto@gmail.com"))

                for i in range(2,16):
                    db.session.add(Cliente("Cliente " + str(i), "Domicilio " + str(i), "Ciudad " + str(i), "Estado " + str(i), "CP" + str(1000+i), "email" + str(i) + "@gmail.com"))
                db.session.commit()

                # Poblar productos
                # descripcion, precio, marca, existencia
                db.session.add(Producto("Producto especial", 15.8,"DMarca", 0))

                for i in range(2,16):
                    db.session.add(Producto("Producto " + str(i), round(random.uniform(10, 100), 2), "Marca " + str(i), random.randint(0, 10)))
                db.session.commit()

                #Poblar proveedores
                for i in range(1,16):
                    db.session.add(Proveedor("Empresa " + str(i), "Contacto " + str(i), "Direccion " + str(i), "Ciudad " + str(i), "Estado" + str(i), "CP" + str(1000+i), "email" + str(i) + "@gmail.com"))
                db.session.commit()

                #Poblar pedidos
                fecha_pedido = datetime.strptime("2023/02/24", "%Y/%m/%d")
                db.session.add(Pedido("Super vendedor", fecha_pedido, 2, 10, 12.36))

                for i in range(2,16):
                    db.session.add(Pedido("Vendedor " + str(i), datetime.now().date(), random.randint(1, 15), random.randint(1, 50), round(random.uniform(30, 300), 2)))
                db.session.commit()

            elif choice == 2:
                print("\n1. Buscar a todos los clientes su nombre empiece con E.")
                clientes_e = Cliente.query.filter(Cliente.nombre.like('E%')).all()
                for c in clientes_e:
                    print(c)
                
                print("\n2. Buscar los proveedores que su correo contenga al menos una letra a.")
                proveedores_a = Proveedor.query.filter(Proveedor.email.like('%a%')).all()
                for p in proveedores_a:
                    print(p)
                
                print("\n3. Buscar los productos que tengan existencia.")
                productos_existentes = Producto.query.filter(Producto.existencia > 0).all()
                for p in productos_existentes:
                    print(p)

                print("\n4. Buscar los productos que la marca empiece con D.")
                productos_marcad = Producto.query.filter(Producto.marca.like('D%')).all()
                for p in productos_marcad:
                    print(p)
                
                print("\n5. Buscar los pedidos que la su fecha sea entre 24/01/2023 al 24/04/2023.")
                fecha_inicio = datetime(2023, 1, 24)
                fecha_fin = datetime(2023, 4, 24)

                pedidos_fecha = Pedido.query.filter(and_(Pedido.fechaPedido >= fecha_inicio, Pedido.fechaPedido <= fecha_fin)).all()
                for p in pedidos_fecha:
                    print(p)
                
                print("\n6. Inventar una consulta, con la tabla proveedores, al menos deberá tener una condición esta consulta.")
                print("   Arrojar proveedores con id entre 4 y 9 (inclusivos).")
                proveedores5_10 = Proveedor.query.filter(and_(Proveedor.id >= 4, Proveedor.id <= 9))
                for p in proveedores5_10:
                    print(p)
            
            elif choice == 3:
                print("Se deberán actualizar 4 datos de cualquier tabla y mostrar los registros modificados.")
                print("Actualizar el nombre del cliente 2 a Erika")
                cliente2 = Cliente.query.filter(Cliente.id == 2)[0]
                cliente2.nombre = "Erika"
                db.session.commit()
                cliente2 = Cliente.query.filter(Cliente.id == 2)[0]
                print(cliente2)

                print("\nActualizar el nombre de la empresa del proveedor 5 a IngSoft")
                proveedor5 = Proveedor.query.filter(Proveedor.id == 5)[0]
                proveedor5.empresa = "IngSoft"
                db.session.commit()
                proveedor5 = Proveedor.query.filter(Proveedor.id == 5)[0]
                print(proveedor5)

                print("\nActualizar el correo del proveedor 1 a proveedor1@exmple.com")
                proveedor1 = Proveedor.query.filter(Proveedor.id == 1)[0]
                proveedor1.email = "proveedor1@exmple.com"
                db.session.commit()
                proveedor1 = Proveedor.query.filter(Proveedor.id == 1)[0]
                print(proveedor1)

                print("\nActualizar la existencia del producto 2 a 0")
                producto2 = Producto.query.filter(Producto.id == 2)[0]
                producto2.existencia = 0
                db.session.commit()
                producto2 = Producto.query.filter(Producto.id == 2)[0]
                print(producto2)

            elif choice == 4:
                print("Se deberán eliminar al menos 5 datos de cualquier tabla.")
                print("Eliminar los últimos 5 datos de proveedores.")
                proveedores = Proveedor.query.all()
                for p in proveedores:
                    if p.id in [10, 11, 12, 13, 14, 15]:
                        db.session.delete(p)
                
                db.session.commit()

            else:
                print("Programa finalizado.")
                





