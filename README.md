# sqlalchemy
This project is a Python application developed using the Flask framework and the SQLAlchemy library to interact with a MySQL database. The main objective of this project is to perform CRUD (Create, Read, Update, and Delete) operations on a database that contains information about clients, products, suppliers, and orders. Below is a detailed description of how this project works and how to use it.

## Prerequisites

Make sure you have the following prerequisites installed in your development environment:

- Python
- Flask
- SQLAlchemy
- A MySQL database
- pymysql library
- cryptography

## Running the Application

To run the application, follow these steps:

1. Open a terminal and navigate to the directory where the `app.py` file is located.

2. Activate your virtual environment (if you are using one).

3. Run the following command to start the application:

   ```
   python app.py
   ```

## Main Features

The application offers the following main features:

### 1. Populate Records

Select option 1 from the menu to populate the database with 15 records for each of the following tables: Clients, Products, Suppliers, and Orders. The data is generated randomly for demonstration purposes.

### 2. Display Query Results

Select option 2 from the menu to perform various queries on the database and display the results. Queries include searching for clients whose names start with "E," suppliers with emails containing the letter "a," products with stock, products with brands starting with "D," orders within a date range, and a custom query that shows suppliers with IDs between 4 and 9.

### 3. Update Data

Select option 3 from the menu to update data in the database. Updates include changing a client's name, a supplier's company name, a supplier's email, and a product's stock. The updated records are displayed after the update.

### 4. Delete Data

Select option 4 from the menu to delete at least 5 records from any table. In the provided example, the last 5 records from the suppliers' table are deleted.

### 5. Exit

Select option 5 from the menu to exit the application.