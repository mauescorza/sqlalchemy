CREATE SCHEMA ejercicio2;
USE ejercicio2;
CREATE USER 'mauescorza'@'localhost' IDENTIFIED BY 'Ejercicio2!';
GRANT ALL ON *.* TO 'mauescorza'@'localhost';
FLUSH PRIVILEGES;

-- Crear la tabla "clientes"
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    domicilio VARCHAR(50),
    ciudad VARCHAR(25),
    estado VARCHAR(25),
    codigoPostal VARCHAR(10),
    email VARCHAR(25)
);

-- Crear la tabla "productos"
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    marca VARCHAR(25),
    existencia INT
);

-- Crear la tabla "proveedores"
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empresa VARCHAR(50) NOT NULL,
    nombreContacto VARCHAR(50),
    direccion VARCHAR(50),
    ciudad VARCHAR(25),
    estado VARCHAR(25),
    codigoPostal VARCHAR(10),
    email VARCHAR(255)
);

-- Crear la tabla "pedidos"
CREATE TABLE pedidos (
    numeroPedido INT AUTO_INCREMENT PRIMARY KEY,
    vendedor VARCHAR(50) NOT NULL,
    fechaPedido DATE NOT NULL,
    producto INT,
    cantidad INT,
    precio DECIMAL(10, 2),
    total DECIMAL(10, 2),
    FOREIGN KEY (producto) REFERENCES productos(id)
);