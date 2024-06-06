DROP DATABASE IF EXISTS order_mgmt;

CREATE DATABASE order_mgmt;

USE order_mgmt;

CREATE TABLE orders (
  order_id VARCHAR(255) NOT NULL,
  order_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id)
);

CREATE TABLE order_customer_details (
  order_id VARCHAR(255) NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  customer_phone VARCHAR(255) NOT NULL,
  customer_address VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE order_items (
  order_id VARCHAR(255) NOT NULL,
  item_ordered VARCHAR(255) NOT NULL,
  PRIMARY KEY(order_id, item_ordered),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE couriers (
  courier_id VARCHAR(255) NOT NULL,
  courier_name VARCHAR(255) NOT NULL,
  courier_phone VARCHAR(255) NOT NULL,
  courier_status VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id)
);

CREATE TABLE courier_delivery_details (
  courier_id VARCHAR(255) NOT NULL,
  order_id VARCHAR(255) NOT NULL,
  PRIMARY KEY(courier_id, order_id),
  FOREIGN KEY (courier_id) REFERENCES couriers(courier_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE items (
  id VARCHAR(255) NOT NULL,
  item VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY(id)
);