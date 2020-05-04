-- This file contains the definitions of the tables used in the application.
--
-- Login table
CREATE TABLE login (login_id serial primary key, username varchar(30), password varchar(30), 
user_id integer references users(user_id));

-- Users table
CREATE TABLE users (user_id serial primary key, user_firstname varchar(20), user_lastname varchar(20), 
user_date_birth char(10), user_email varchar(30));

-- User Phone table
CREATE TABLE user_phone (phone_id serial primary key, user_id integer references users(user_id), user_phone char(10));

-- Supplier table
CREATE TABLE supplier (supplier_id serial primary key, user_id integer references users(user_id));

-- Customer table
CREATE TABLE customer (customer_id serial primary key, user_id integer references users(user_id));

-- Admin table
CREATE TABLE admin (admin_id serial primary key, user_id integer references users(user_id));

-- Manages table 
CREATE TABLE manages (user_id integer references users(user_id), admin_id integer references admin(admin_id), 
primary key (user_id, admin_id));

-- Address table
CREATE TABLE address (address_id serial primary key, user_id integer references users(user_id), addressline varchar(40), 
city varchar(20), state_province varchar(20), country varchar(20), zipcode char(5));

-- Company table
CREATE TABLE company (company_id serial primary key, company_name varchar(20), company_address varchar(50), 
company_phone char(10));

-- Represents table
CREATE TABLE represents (company_id integer references company(company_id), supplier_id integer references 
supplier(supplier_id), primary key (company_id, supplier_id));

-- Payment table
CREATE TABLE payment (payment_id serial primary key, customer_id integer references customer(customer_id));

-- Credit card table
CREATE TABLE creditcard (creditcard_id serial primary key, payment_id integer references payment(payment_id), 
creditcard_name varchar(20), creditcard_number char(16), creditcard_ccv char(3), creditcard_exp_date char(5));

-- PayPal table
CREATE TABLE paypal (paypal_id serial primary key, payment_id integer references payment(payment_id), 
paypal_username varchar(20), paypal_password varchar(20));

-- Ath Movil table
CREATE TABLE ath_movil (ath_movil_id serial primary key, payment_id integer references payment(payment_id), 
ath_movil_phone char(10));

-- Resource table
CREATE TABLE resource (resource_id serial primary key, supplier_id integer references supplier(supplier_id), 
resource_category varchar(20), resource_name varchar(20), resource_brand varchar(20), resource_quantity integer, 
resource_price float);

-- Request table
CREATE TABLE request (request_id serial primary key, customer_id integer references customer(customer_id), 
request_title varchar(40), request_date char(10));

-- Resource Requests table
CREATE TABLE resource_requests (request_id integer references request(request_id), resource_id integer references 
resource(resource_id), primary key (request_id, resource_id), request_quantity integer);

-- Reservation table
CREATE TABLE reservation (reservation_id serial primary key, customer_id integer references customer(customer_id), 
reservation_date char(10), reservation_status varchar(10));

-- Resource Reservations table
CREATE TABLE resource_reservations (reservation_id integer references reservation(reservation_id), resource_id 
integer references resource(resource_id), primary key (reservation_id, resource_id), reservation_quantity integer);

-- Order table
CREATE TABLE order (order_id serial primary key, customer_id integer references customer(customer_id), 
payment_id integer references payment(payment_id), order_date char(10), order_price float, order_status varchar(10));

-- Resource Orders table
CREATE TABLE resource_orders (order_id integer references order(order_id), resource_id integer references 
resource(resource_id), primary key (order_id, resource_id), discount float, order_quantity integer);

-- Fuel table
CREATE TABLE fuel (fuel_id serial primary key, resource_id integer references resource(resource_id), 
fuel_type varchar(10), fuel_gallons float);

-- Food table
CREATE TABLE food (food_id serial primary key, resource_id integer references resource(resource_id), 
food_category varchar(15), food_container varchar(15), food_type varchar(15), food_expdate char(10), food_ounces float);

-- Medicine table
CREATE TABLE medicine (med_id serial primary key, resource_id integer references resource(resource_id), 
med_type varchar(15), med_dose varchar(10), med_prescript char(1), med_expdate char(10));

-- Tools table
CREATE TABLE tools (tool_id serial primary key, resource_id integer references resource(resource_id), 
tool_material varchar(20), tool_condition varchar(10), tool_pwtype varchar(10));

-- Medical device table
CREATE TABLE medical_device (med_device_id serial primary key, resource_id integer references resource(resource_id), 
med_device_type varchar(15), med_device_model varchar(10), med_device_condition varchar(10), 
med_device_power_type varchar(10));

-- Water table
CREATE TABLE water (water_id serial primary key, resource_id integer references resource(resource_id), 
water_size varchar(10), water_container varchar(10), water_type varchar(10), water_exp_date char(10));

-- Cloth table
CREATE TABLE cloth (cloth_id serial primary key, resource_id integer references resource(resource_id), 
cloth_size varchar(5), cloth_material varchar(10), cloth_condition varchar(10), cloth_gender varchar(10), 
cloth_category varchar(10));

-- Heavy equipment table
CREATE TABLE heavy_equipment (heavyequip_id serial primary key, resource_id integer references resource(resource_id), 
heavyequip_type varchar(15), heavyequip_model varchar(10), heavyequip_condition varchar(10));

-- Ice table
CREATE TABLE ice (ice_id serial primary key, resource_id integer references resource(resource_id), ice_weight varchar(10));

-- Generators table
CREATE TABLE generators (generator_id serial primary key, resource_id integer references resource(resource_id), 
power_capacity varchar(10), power_condition varchar(10), generator_fuel varchar(10));

-- Batteries table
CREATE TABLE batteries (battery_id serial primary key, resource_id integer references resource(resource_id), 
power_capacity varchar(10), power_condition varchar(10), battery_type varchar(10));
