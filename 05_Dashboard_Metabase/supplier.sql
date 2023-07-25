--REGION DATABASE
drop table if EXISTS region;
CREATE TABLE region(
    region_id serial PRIMARY KEY,
    region_description varchar(50)
);

\COPY region(region_id,region_description) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/regions.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';


--SUPPLIER DATABASE
drop table if EXISTS supplier;
CREATE TABLE supplier(
    supplier_id INT PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100),
    contact_title varchar(100),
    supplier_address varchar(100),
    city  varchar(50),
    region varchar(50),
    postalCode varchar(50),
    country varchar(50),
    phone varchar(50),
    fax varchar(50),
    homePage text
);

\COPY supplier(supplier_id,company_name,contact_name,contact_title,supplier_address,city,region,postalCode,country,phone,fax,homePage) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/suppliers.csv' DELIMITER ',' CSV HEADER null as 'NULL';

--SHIPPER DATABASE
drop table if EXISTS shipper;
CREATE TABLE shipper(
    shipper_id int PRIMARY KEY,
     company_name text,
     phone text
);

\COPY shipper(shipper_id,company_name,phone) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/shippers.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';

--TERRITORIES DATABASE
DROP table if EXISTS territories;
create table territories(
    territory_id int PRIMARY KEY,
    territory_description text,
    region_id int
);

\COPY territories(territory_id,territory_description,region_id) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/territories.csv' DELIMITER ',' CSV HEADER NULL as 'null';

--CATEGORIES DATABASE
drop table if EXISTS categories;
create table categories(
category_id int PRIMARY key,
category_name varchar(50),
cat_description text,
picture bytea
);
\COPY categories(category_id,category_name,cat_description,picture) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/categories.csv' DELIMITER ',' csv HEADER NULL as 'NULL';


--customer database
drop table if EXISTS customer;
create table customer(
    customer_id varchar(50) not null,
    company_name varchar(50) not null,
    contact_name varchar(50),
    contact_title varchar(50),
    customer_address varchar(50),
    city varchar(50),
    region varchar(50),
    postal_code varchar(50),
    country varchar(50),
    phone varchar(50),
    fax varchar(50)
);

\COPY customer(customer_id,company_name,contact_name,contact_title,customer_address,city,region,postal_code,country,phone,fax) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/customers.csv' DELIMITER ',' csv HEADER NULL as 'NULL';

--emply_terri database
drop table if EXISTS employee_territories;
CREATE TABLE employee_territories(
    employee_id int not null,
    territory_id int not NULL
);
\COPY employee_territories(employee_id,territory_id) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/employee_territories.csv' DELIMITER ',' CSV HEADER NULL as 'NULL';

--employee database
drop table if EXISTS employee;
CREATE TABLE employee(
    employee_id int PRIMARY key,
    last_name text,
    first_name text,
    title text,
    title_of_courtesy text,
    birth_date timestamp,
    hire_date timestamp,
    employee_address varchar(100),
    city varchar(100),
    region varchar(50),
    postal_code varchar(50),
    country varchar(50),
    home_phone varchar(50),
    extension int,
    photo text,
    notes text,
    reports_to INT,
    photo_path text
);

\COPY employee(employee_id,last_name,first_name,title,title_of_courtesy,birth_date,hire_date,employee_address,city,region,postal_code,country,home_phone,extension,photo,notes,reports_to,photo_path) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/employees.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';

--order_detail database
 drop table if EXISTS order_details;
 CREATE TABLE order_details(
    order_id INT ,
    product_id int,
    unit_price float,
    quantity int,
    discount float
 );
\COPY order_details(order_id,product_id,unit_price,quantity,discount) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/order_details.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';

--order database
drop table if EXISTS orders;
CREATE TABLE orders(
    order_id int,
    customer_id varchar,
    employee_id int,
    order_date timestamp,
    required_date timestamp,
    shipped_date timestamp,
    ship_via int,
    freight float,
    ship_name text,
    ship_address text,
    ship_city text,
    ship_region text,
    ship_postal_code text,
    ship_country text
);

\COPY orders(order_id,customer_id,employee_id,order_date,required_date,shipped_date,ship_via,freight,ship_name,ship_address,ship_city,ship_region,ship_postal_code,ship_country) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/orders.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';

--product database
drop table if EXISTS products;
CREATE TABLE products(
    product_id int,
    product_name text,
    supplier_id int,
    category_id int,
    quantity_per_unit text,
    unit_price float,
    units_in_stock int,
    units_on_order int,
    reorder_level int,
    discontinued int
);

\COPY products(product_id,product_name,supplier_id,category_id,quantity_per_unit,unit_price,units_in_stock,units_on_order,reorder_level,discontinued) FROM '/Users/akshayrote/Documents/spiced_Acadamy/Daily_Task/week05/North_wind_data/products.csv'  DELIMITER ',' CSV HEADER NULL AS 'NULL';


 

 