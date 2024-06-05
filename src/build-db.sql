DROP DATABASE IF EXISTS order_mgmt;

CREATE DATABASE order_mgmt;

USE order_mgmt;

CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  items VARCHAR(255) NOT NULL,
  order_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id),
  UNIQUE KEY (customer_phone),  -- Ensuring customer_phone is unique for the FK
  UNIQUE KEY (customer_address)
);

CREATE TABLE couriers (
  courier_id INT NOT NULL AUTO_INCREMENT,
  order_id INT,
  courier_name VARCHAR(255) NOT NULL,
  target_address VARCHAR(255),
  courier_phone VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  courier_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id),
  FOREIGN KEY(target_address) REFERENCES orders(customer_address),
  FOREIGN KEY(order_id) REFERENCES orders(order_id),
  FOREIGN KEY(customer_phone) REFERENCES orders(customer_phone)
);

CREATE TABLE items (
  id INT NOT NULL AUTO_INCREMENT,
  item VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY(id)
);