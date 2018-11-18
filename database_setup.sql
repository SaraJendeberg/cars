-- creates tables in the database

-- Delete the tables if they exist.
-- Disable foreign key checks, so the tables can
-- be dropped in arbitrary order.
PRAGMA foreign_keys=OFF;
drop table if exists sales;
drop table if exists employees;
drop table if exists carmodels;
PRAGMA foreign_keys=ON;

-- create employees
CREATE TABLE employees (
  id INTEGER,
  name VARCHAR (255) NOT NULL,
  PRIMARY KEY (id)
);

-- create carmodels
CREATE TABLE carmodels (
  id INTEGER,
  brand VARCHAR (255) NOT NULL,
  model VARCHAR (255) NOT NULL,
  price INTEGER NOT NULL,
  PRIMARY KEY (id)
);

-- create sales
CREATE TABLE sales (
  id INTEGER,
  employee_id INT,
  carmodel_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (employee_id) REFERENCES employees (id),
  FOREIGN KEY (carmodel_id) REFERENCES carmodels(id)
);

-- INSERT THE DATA
INSERT INTO employees(id, name)
VALUES(1, 'Hjulia Styrén'),
      (2, 'Antonia Cylinder'),
      (3, 'Kalle Bromslöf'),
      (4, 'Johan Sportratt');

INSERT INTO carmodels(id, brand, model, price)
VALUES(1, 'BMW', '335i', 200000),
      (2, 'Aston Martin', 'Vanquish', 233000),
      (3, 'Toyota', 'Prius', 150000),
      (4, 'Volvo', '240', 100000);

INSERT INTO sales(id, employee_id, carmodel_id)
VALUES(1, 2, 3),
      (2, 4, 2),
      (3, 4, 4),
      (4, 1, 1),
      (5, 3, 1),
      (6, 3, 1),
      (7, 2, 2),
      (8, 2, 3);
