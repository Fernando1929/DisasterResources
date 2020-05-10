--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.17
-- Dumped by pg_dump version 9.6.17

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: address; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.address (
    address_id integer NOT NULL,
    user_id integer,
    addressline character varying(40),
    city character varying(20),
    state_province character varying(20),
    country character varying(20),
    zipcode character(5)
);


ALTER TABLE public.address OWNER TO postgres;

--
-- Name: address_address_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.address_address_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.address_address_id_seq OWNER TO postgres;

--
-- Name: address_address_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.address_address_id_seq OWNED BY public.address.address_id;


--
-- Name: admin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.admin (
    admin_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.admin OWNER TO postgres;

--
-- Name: admin_admin_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.admin_admin_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.admin_admin_id_seq OWNER TO postgres;

--
-- Name: admin_admin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.admin_admin_id_seq OWNED BY public.admin.admin_id;


--
-- Name: ath_movil; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ath_movil (
    ath_movil_id integer NOT NULL,
    payment_id integer,
    ath_movil_phone character(10)
);


ALTER TABLE public.ath_movil OWNER TO postgres;

--
-- Name: ath_movil_ath_movil_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ath_movil_ath_movil_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ath_movil_ath_movil_id_seq OWNER TO postgres;

--
-- Name: ath_movil_ath_movil_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ath_movil_ath_movil_id_seq OWNED BY public.ath_movil.ath_movil_id;


--
-- Name: batteries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.batteries (
    battery_id integer NOT NULL,
    resource_id integer,
    power_capacity character varying(10),
    power_condition character varying(10),
    battery_type character varying(10)
);


ALTER TABLE public.batteries OWNER TO postgres;

--
-- Name: batteries_battery_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.batteries_battery_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.batteries_battery_id_seq OWNER TO postgres;

--
-- Name: batteries_battery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.batteries_battery_id_seq OWNED BY public.batteries.battery_id;


--
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    category_id integer NOT NULL,
    category_name character varying(20)
);


ALTER TABLE public.category OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_category_id_seq OWNER TO postgres;

--
-- Name: category_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_category_id_seq OWNED BY public.category.category_id;


--
-- Name: cloth; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cloth (
    cloth_id integer NOT NULL,
    resource_id integer,
    cloth_size character varying(10),
    cloth_material character varying(15),
    cloth_condition character varying(10),
    cloth_gender character varying(10),
    cloth_type character varying(15)
);


ALTER TABLE public.cloth OWNER TO postgres;

--
-- Name: cloth_cloth_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cloth_cloth_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cloth_cloth_id_seq OWNER TO postgres;

--
-- Name: cloth_cloth_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cloth_cloth_id_seq OWNED BY public.cloth.cloth_id;


--
-- Name: company; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.company (
    company_id integer NOT NULL,
    company_name character varying(20),
    company_address character varying(50),
    company_phone character(10)
);


ALTER TABLE public.company OWNER TO postgres;

--
-- Name: company_company_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.company_company_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.company_company_id_seq OWNER TO postgres;

--
-- Name: company_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.company_company_id_seq OWNED BY public.company.company_id;


--
-- Name: creditcard; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.creditcard (
    creditcard_id integer NOT NULL,
    payment_id integer,
    creditcard_name character varying(30),
    creditcard_number character(16),
    creditcard_ccv character(3),
    creditcard_exp_date character(5)
);


ALTER TABLE public.creditcard OWNER TO postgres;

--
-- Name: creditcard_creditcard_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.creditcard_creditcard_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.creditcard_creditcard_id_seq OWNER TO postgres;

--
-- Name: creditcard_creditcard_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.creditcard_creditcard_id_seq OWNED BY public.creditcard.creditcard_id;


--
-- Name: customer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.customer (
    customer_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.customer OWNER TO postgres;

--
-- Name: customer_customer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.customer_customer_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_customer_id_seq OWNER TO postgres;

--
-- Name: customer_customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.customer_customer_id_seq OWNED BY public.customer.customer_id;


--
-- Name: food; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.food (
    food_id integer NOT NULL,
    resource_id integer,
    food_category character varying(15),
    food_container character varying(15),
    food_type character varying(15),
    food_expdate character(10),
    food_ounces double precision
);


ALTER TABLE public.food OWNER TO postgres;

--
-- Name: food_food_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.food_food_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.food_food_id_seq OWNER TO postgres;

--
-- Name: food_food_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.food_food_id_seq OWNED BY public.food.food_id;


--
-- Name: fuel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.fuel (
    fuel_id integer NOT NULL,
    resource_id integer,
    fuel_type character varying(10),
    fuel_gallons double precision
);


ALTER TABLE public.fuel OWNER TO postgres;

--
-- Name: fuel_fuel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.fuel_fuel_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fuel_fuel_id_seq OWNER TO postgres;

--
-- Name: fuel_fuel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.fuel_fuel_id_seq OWNED BY public.fuel.fuel_id;


--
-- Name: generators; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.generators (
    generator_id integer NOT NULL,
    resource_id integer,
    power_capacity character varying(10),
    power_condition character varying(10),
    generator_fuel character varying(10)
);


ALTER TABLE public.generators OWNER TO postgres;

--
-- Name: generators_generator_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.generators_generator_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.generators_generator_id_seq OWNER TO postgres;

--
-- Name: generators_generator_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.generators_generator_id_seq OWNED BY public.generators.generator_id;


--
-- Name: heavy_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.heavy_equipment (
    heavyequip_id integer NOT NULL,
    resource_id integer,
    heavyequip_type character varying(30),
    heavyequip_model character varying(10),
    heavyequip_condition character varying(10)
);


ALTER TABLE public.heavy_equipment OWNER TO postgres;

--
-- Name: heavy_equipment_heavyequip_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.heavy_equipment_heavyequip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.heavy_equipment_heavyequip_id_seq OWNER TO postgres;

--
-- Name: heavy_equipment_heavyequip_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.heavy_equipment_heavyequip_id_seq OWNED BY public.heavy_equipment.heavyequip_id;


--
-- Name: ice; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ice (
    ice_id integer NOT NULL,
    resource_id integer,
    ice_weight character varying(10)
);


ALTER TABLE public.ice OWNER TO postgres;

--
-- Name: ice_ice_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ice_ice_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ice_ice_id_seq OWNER TO postgres;

--
-- Name: ice_ice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ice_ice_id_seq OWNED BY public.ice.ice_id;


--
-- Name: login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.login (
    login_id integer NOT NULL,
    username character varying(30),
    password character varying(30),
    user_id integer
);


ALTER TABLE public.login OWNER TO postgres;

--
-- Name: login_login_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.login_login_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.login_login_id_seq OWNER TO postgres;

--
-- Name: login_login_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.login_login_id_seq OWNED BY public.login.login_id;


--
-- Name: manages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.manages (
    user_id integer NOT NULL,
    admin_id integer NOT NULL
);


ALTER TABLE public.manages OWNER TO postgres;

--
-- Name: medical_device; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medical_device (
    med_device_id integer NOT NULL,
    resource_id integer,
    med_device_type character varying(30),
    med_device_model character varying(15),
    med_device_condition character varying(10),
    med_device_power_type character varying(10)
);


ALTER TABLE public.medical_device OWNER TO postgres;

--
-- Name: medical_device_med_device_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medical_device_med_device_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medical_device_med_device_id_seq OWNER TO postgres;

--
-- Name: medical_device_med_device_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medical_device_med_device_id_seq OWNED BY public.medical_device.med_device_id;


--
-- Name: medicine; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.medicine (
    med_id integer NOT NULL,
    resource_id integer,
    med_type character varying(15),
    med_dose character varying(10),
    med_prescript character(1),
    med_expdate character(10)
);


ALTER TABLE public.medicine OWNER TO postgres;

--
-- Name: medicine_med_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.medicine_med_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.medicine_med_id_seq OWNER TO postgres;

--
-- Name: medicine_med_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.medicine_med_id_seq OWNED BY public.medicine.med_id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    customer_id integer,
    payment_id integer,
    order_date character(10),
    order_price double precision,
    order_status character varying(10),
    request_id integer
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.orders_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders_order_id_seq OWNER TO postgres;

--
-- Name: orders_order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.orders_order_id_seq OWNED BY public.orders.order_id;


--
-- Name: payment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment (
    payment_id integer NOT NULL,
    customer_id integer
);


ALTER TABLE public.payment OWNER TO postgres;

--
-- Name: payment_payment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payment_payment_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.payment_payment_id_seq OWNER TO postgres;

--
-- Name: payment_payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.payment_payment_id_seq OWNED BY public.payment.payment_id;


--
-- Name: paypal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paypal (
    paypal_id integer NOT NULL,
    payment_id integer,
    paypal_username character varying(20),
    paypal_password character varying(20)
);


ALTER TABLE public.paypal OWNER TO postgres;

--
-- Name: paypal_paypal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paypal_paypal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paypal_paypal_id_seq OWNER TO postgres;

--
-- Name: paypal_paypal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paypal_paypal_id_seq OWNED BY public.paypal.paypal_id;


--
-- Name: represents; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.represents (
    company_id integer NOT NULL,
    supplier_id integer NOT NULL
);


ALTER TABLE public.represents OWNER TO postgres;

--
-- Name: request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.request (
    request_id integer NOT NULL,
    customer_id integer,
    request_title character varying(40),
    request_date character(10),
    request_description text,
    request_status character varying(10)
);


ALTER TABLE public.request OWNER TO postgres;

--
-- Name: request_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.request_category (
    request_id integer NOT NULL,
    category_id integer NOT NULL,
    request_quantity integer
);


ALTER TABLE public.request_category OWNER TO postgres;

--
-- Name: request_request_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.request_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.request_request_id_seq OWNER TO postgres;

--
-- Name: request_request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.request_request_id_seq OWNED BY public.request.request_id;


--
-- Name: reservation; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reservation (
    reservation_id integer NOT NULL,
    customer_id integer,
    reservation_date character(10),
    reservation_status character varying(10),
    request_id integer
);


ALTER TABLE public.reservation OWNER TO postgres;

--
-- Name: reservation_reservation_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reservation_reservation_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reservation_reservation_id_seq OWNER TO postgres;

--
-- Name: reservation_reservation_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reservation_reservation_id_seq OWNED BY public.reservation.reservation_id;


--
-- Name: resource; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resource (
    resource_id integer NOT NULL,
    supplier_id integer,
    category_id integer,
    resource_name character varying(50),
    resource_brand character varying(50),
    resource_quantity integer,
    resource_price double precision
);


ALTER TABLE public.resource OWNER TO postgres;

--
-- Name: resource_orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resource_orders (
    order_id integer NOT NULL,
    resource_id integer NOT NULL,
    discount double precision,
    order_quantity integer
);


ALTER TABLE public.resource_orders OWNER TO postgres;

--
-- Name: resource_reservations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.resource_reservations (
    reservation_id integer NOT NULL,
    resource_id integer NOT NULL,
    reservation_quantity integer
);


ALTER TABLE public.resource_reservations OWNER TO postgres;

--
-- Name: resource_resource_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.resource_resource_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resource_resource_id_seq OWNER TO postgres;

--
-- Name: resource_resource_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.resource_resource_id_seq OWNED BY public.resource.resource_id;


--
-- Name: supplier; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.supplier (
    supplier_id integer NOT NULL,
    user_id integer
);


ALTER TABLE public.supplier OWNER TO postgres;

--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.supplier_supplier_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.supplier_supplier_id_seq OWNER TO postgres;

--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.supplier_supplier_id_seq OWNED BY public.supplier.supplier_id;


--
-- Name: tools; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tools (
    tool_id integer NOT NULL,
    resource_id integer,
    tool_material character varying(20),
    tool_condition character varying(10),
    tool_pwtype character varying(10)
);


ALTER TABLE public.tools OWNER TO postgres;

--
-- Name: tools_tool_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tools_tool_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tools_tool_id_seq OWNER TO postgres;

--
-- Name: tools_tool_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tools_tool_id_seq OWNED BY public.tools.tool_id;


--
-- Name: user_phone; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_phone (
    phone_id integer NOT NULL,
    user_id integer,
    user_phone character(10)
);


ALTER TABLE public.user_phone OWNER TO postgres;

--
-- Name: user_phone_phone_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_phone_phone_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_phone_phone_id_seq OWNER TO postgres;

--
-- Name: user_phone_phone_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_phone_phone_id_seq OWNED BY public.user_phone.phone_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    user_firstname character varying(20),
    user_lastname character varying(20),
    user_date_birth character(10),
    user_email character varying(30)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO postgres;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: water; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.water (
    water_id integer NOT NULL,
    resource_id integer,
    water_size character varying(10),
    water_container character varying(10),
    water_type character varying(10),
    water_exp_date character(10)
);


ALTER TABLE public.water OWNER TO postgres;

--
-- Name: water_water_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.water_water_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.water_water_id_seq OWNER TO postgres;

--
-- Name: water_water_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.water_water_id_seq OWNED BY public.water.water_id;


--
-- Name: address address_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address ALTER COLUMN address_id SET DEFAULT nextval('public.address_address_id_seq'::regclass);


--
-- Name: admin admin_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin ALTER COLUMN admin_id SET DEFAULT nextval('public.admin_admin_id_seq'::regclass);


--
-- Name: ath_movil ath_movil_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ath_movil ALTER COLUMN ath_movil_id SET DEFAULT nextval('public.ath_movil_ath_movil_id_seq'::regclass);


--
-- Name: batteries battery_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.batteries ALTER COLUMN battery_id SET DEFAULT nextval('public.batteries_battery_id_seq'::regclass);


--
-- Name: category category_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN category_id SET DEFAULT nextval('public.category_category_id_seq'::regclass);


--
-- Name: cloth cloth_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cloth ALTER COLUMN cloth_id SET DEFAULT nextval('public.cloth_cloth_id_seq'::regclass);


--
-- Name: company company_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company ALTER COLUMN company_id SET DEFAULT nextval('public.company_company_id_seq'::regclass);


--
-- Name: creditcard creditcard_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.creditcard ALTER COLUMN creditcard_id SET DEFAULT nextval('public.creditcard_creditcard_id_seq'::regclass);


--
-- Name: customer customer_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer ALTER COLUMN customer_id SET DEFAULT nextval('public.customer_customer_id_seq'::regclass);


--
-- Name: food food_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.food ALTER COLUMN food_id SET DEFAULT nextval('public.food_food_id_seq'::regclass);


--
-- Name: fuel fuel_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fuel ALTER COLUMN fuel_id SET DEFAULT nextval('public.fuel_fuel_id_seq'::regclass);


--
-- Name: generators generator_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generators ALTER COLUMN generator_id SET DEFAULT nextval('public.generators_generator_id_seq'::regclass);


--
-- Name: heavy_equipment heavyequip_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heavy_equipment ALTER COLUMN heavyequip_id SET DEFAULT nextval('public.heavy_equipment_heavyequip_id_seq'::regclass);


--
-- Name: ice ice_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ice ALTER COLUMN ice_id SET DEFAULT nextval('public.ice_ice_id_seq'::regclass);


--
-- Name: login login_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login ALTER COLUMN login_id SET DEFAULT nextval('public.login_login_id_seq'::regclass);


--
-- Name: medical_device med_device_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_device ALTER COLUMN med_device_id SET DEFAULT nextval('public.medical_device_med_device_id_seq'::regclass);


--
-- Name: medicine med_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicine ALTER COLUMN med_id SET DEFAULT nextval('public.medicine_med_id_seq'::regclass);


--
-- Name: orders order_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders ALTER COLUMN order_id SET DEFAULT nextval('public.orders_order_id_seq'::regclass);


--
-- Name: payment payment_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment ALTER COLUMN payment_id SET DEFAULT nextval('public.payment_payment_id_seq'::regclass);


--
-- Name: paypal paypal_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paypal ALTER COLUMN paypal_id SET DEFAULT nextval('public.paypal_paypal_id_seq'::regclass);


--
-- Name: request request_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request ALTER COLUMN request_id SET DEFAULT nextval('public.request_request_id_seq'::regclass);


--
-- Name: reservation reservation_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservation ALTER COLUMN reservation_id SET DEFAULT nextval('public.reservation_reservation_id_seq'::regclass);


--
-- Name: resource resource_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource ALTER COLUMN resource_id SET DEFAULT nextval('public.resource_resource_id_seq'::regclass);


--
-- Name: supplier supplier_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.supplier ALTER COLUMN supplier_id SET DEFAULT nextval('public.supplier_supplier_id_seq'::regclass);


--
-- Name: tools tool_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tools ALTER COLUMN tool_id SET DEFAULT nextval('public.tools_tool_id_seq'::regclass);


--
-- Name: user_phone phone_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_phone ALTER COLUMN phone_id SET DEFAULT nextval('public.user_phone_phone_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: water water_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.water ALTER COLUMN water_id SET DEFAULT nextval('public.water_water_id_seq'::regclass);


--
-- Data for Name: address; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.address (address_id, user_id, addressline, city, state_province, country, zipcode) FROM stdin;
1	1	25052 Sutherland Hill	Utuado	Puerto Rico	USA	85925
2	2	911 Claremont Junction	Vieques	Puerto Rico	USA	97060
3	3	2941 Morrow Lane	Las Piedras	Puerto Rico	USA	14864
4	4	934 Starling Street	Canóvanas	Puerto Rico	USA	21913
5	5	9644 Grasskamp Alley	Patillas	Puerto Rico	USA	55480
6	6	26 Harper Alley	Morovis	Puerto Rico	USA	30090
7	7	860 Anderson Hill	Comerío	Puerto Rico	USA	78493
8	8	5 Briar Crest Terrace	Hatillo	Puerto Rico	USA	59200
9	9	812 Schiller Point	San Sebastián	Puerto Rico	USA	35207
10	10	36 Gale Street	Florida	Puerto Rico	USA	25959
11	11	9239 Holmberg Crossing	San Sebastián	Puerto Rico	USA	42525
12	12	881 Clarendon Lane	Maricao	Puerto Rico	USA	18601
13	13	6662 Loftsgordon Place	San Juan	Puerto Rico	USA	41141
14	14	884 Dexter Parkway	Loiza	Puerto Rico	USA	70498
15	15	9476 Cottonwood Hill	Barranquitas	Puerto Rico	USA	30479
16	16	3969 Everett Parkway	Carolina	Puerto Rico	USA	22835
17	17	7 Fordem Street	Ceiba	Puerto Rico	USA	54956
18	18	7389 Fairfield Point	Aibonito	Puerto Rico	USA	14295
19	19	5282 Farwell Plaza	Comerío	Puerto Rico	USA	79764
20	20	5 Rockefeller Center	San Germán	Puerto Rico	USA	40163
21	21	9045 Prairie Rose Place	Maunabo	Puerto Rico	USA	44678
22	22	6 Oriole Center	Orocovis	Puerto Rico	USA	45790
23	23	77 Oriole Trail	Arroyo	Puerto Rico	USA	90944
24	24	762 Marcy Trail	Aguas Buenas	Puerto Rico	USA	83193
25	25	09 Autumn Leaf Hill	Lares	Puerto Rico	USA	29930
26	26	4419 Buhler Terrace	Naguabo	Puerto Rico	USA	25207
27	27	6749 Forest Street	Barranquitas	Puerto Rico	USA	18112
28	28	9670 International Trail	Santa Isabel	Puerto Rico	USA	20117
29	29	361 Buena Vista Way	Barranquitas	Puerto Rico	USA	38922
30	30	74 Bluejay Circle	Arecibo	Puerto Rico	USA	23511
31	31	1439 Farragut Parkway	Peñuelas	Puerto Rico	USA	90746
32	32	502 Bay Plaza	Vieques	Puerto Rico	USA	58601
33	33	1 Sugar Way	Sabana Grande	Puerto Rico	USA	53880
34	34	4675 Westport Lane	Corozal	Puerto Rico	USA	17743
35	35	19 Cascade Place	Naguabo	Puerto Rico	USA	89717
36	36	192 Hansons Road	Humacao	Puerto Rico	USA	91765
37	37	7 Truax Parkway	Santa Isabel	Puerto Rico	USA	86325
38	38	6908 Oxford Point	Vieques	Puerto Rico	USA	17100
39	39	88946 Veith Lane	Canóvanas	Puerto Rico	USA	48650
40	40	053 Carberry Parkway	Florida	Puerto Rico	USA	76264
41	41	0 Anhalt Way	Guaynabo	Puerto Rico	USA	75482
42	42	36 Ridgeway Point	San Juan	Puerto Rico	USA	62275
43	43	868 Judy Terrace	Maunabo	Puerto Rico	USA	83218
44	44	932 Dayton Way	San Germán	Puerto Rico	USA	94832
45	45	004 Summer Ridge Park	Naguabo	Puerto Rico	USA	70301
46	46	2 Melvin Place	Orocovis	Puerto Rico	USA	12388
47	47	0850 Northfield Pass	Ceiba	Puerto Rico	USA	93677
48	48	940 Dawn Place	Maricao	Puerto Rico	USA	82866
49	49	0 Bonner Pass	Guánica	Puerto Rico	USA	38143
50	50	5209 Rusk Pass	San Juan	Puerto Rico	USA	47149
51	51	002 Mosinee Avenue	Ceiba	Puerto Rico	USA	23874
52	52	19551 Eggendart Avenue	Carolina	Puerto Rico	USA	81610
53	53	68 Tony Circle	Barceloneta	Puerto Rico	USA	55273
54	54	45 Old Gate Terrace	Florida	Puerto Rico	USA	54056
55	55	58468 Glacier Hill Court	Ciales	Puerto Rico	USA	37147
56	56	0250 Warner Trail	Toa Alta	Puerto Rico	USA	97957
57	57	21 Towne Lane	Cabo Rojo	Puerto Rico	USA	94940
58	58	93 Oak Valley Park	Quebradillas	Puerto Rico	USA	63487
59	59	603 Oakridge Alley	Naguabo	Puerto Rico	USA	61340
60	60	3404 Arkansas Circle	Quebradillas	Puerto Rico	USA	35539
61	61	75 Loomis Way	Bayamón	Puerto Rico	USA	75761
62	62	11127 Messerschmidt Way	Jayuya	Puerto Rico	USA	59958
63	63	9221 Little Fleur Trail	Vega Alta	Puerto Rico	USA	10013
64	64	67369 Lindbergh Street	Isabela	Puerto Rico	USA	50838
65	65	0 Springview Plaza	Lares	Puerto Rico	USA	26218
66	66	34 Cherokee Point	Humacao	Puerto Rico	USA	52160
67	67	05 Green Drive	Humacao	Puerto Rico	USA	72565
68	68	335 Grover Hill	Aibonito	Puerto Rico	USA	77713
69	69	98 Eastlawn Junction	Maunabo	Puerto Rico	USA	13276
70	70	3287 Blue Bill Park Junction	Cayey	Puerto Rico	USA	12281
\.


--
-- Name: address_address_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.address_address_id_seq', 70, true);


--
-- Data for Name: admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.admin (admin_id, user_id) FROM stdin;
1	61
2	62
3	63
4	64
5	65
6	66
7	67
8	68
9	69
10	70
\.


--
-- Name: admin_admin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.admin_admin_id_seq', 10, true);


--
-- Data for Name: ath_movil; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ath_movil (ath_movil_id, payment_id, ath_movil_phone) FROM stdin;
1	1	3154554321
2	2	3150901154
3	3	3157960978
4	4	3159159151
5	5	3151060294
6	6	3159944952
7	7	3150005412
8	8	5040943184
9	9	3165673214
10	10	3167891234
\.


--
-- Name: ath_movil_ath_movil_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ath_movil_ath_movil_id_seq', 10, true);


--
-- Data for Name: batteries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.batteries (battery_id, resource_id, power_capacity, power_condition, battery_type) FROM stdin;
1	81	Used	2600	E
2	82	Used	625	AAAA
3	83	New	400	E
4	84	New	8000	AAA
5	85	New	1200	C
6	86	New	8000	AAAA
7	87	Used	600	Lanter
8	88	Used	850	AAA
9	89	Used	625	Lanter
10	90	Used	2700	AAAA
\.


--
-- Name: batteries_battery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.batteries_battery_id_seq', 10, true);


--
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (category_id, category_name) FROM stdin;
1	fuel
2	food
3	medicine
4	tool
5	cloth
6	heavy_equipment
7	water
8	medical_device
9	battery
10	generator
11	ice
\.


--
-- Name: category_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_category_id_seq', 11, true);


--
-- Data for Name: cloth; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cloth (cloth_id, resource_id, cloth_size, cloth_material, cloth_condition, cloth_gender, cloth_type) FROM stdin;
1	1	M	Cotton	New	Male	T-shirt
2	2	S	Polyster	New	Female	T-shirt
3	3	L	Cotton	Used	Male	Pants
4	4	M	Cotton	New	Male	T-shirt
5	5	9.5	Cotton	New	Male	Shoes
6	6	S	Cotton	New	Female	Polo
7	7	L	Cotton	New	Male	Pants
8	8	M	Cotton	New	Female	T-shirt
9	9	M	Cotton	New	Female	Sweaters
10	10	18-24M	Cotton	New	Female	Baby
\.


--
-- Name: cloth_cloth_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cloth_cloth_id_seq', 10, true);


--
-- Data for Name: company; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.company (company_id, company_name, company_address, company_phone) FROM stdin;
1	Wikizz	192 Pierstorff Drive	7683332410
2	Zoomdog	973 Hazelcrest Center	5672358645
3	Yakijo	63 2nd Crossing	1923795721
4	Yadel	584 Hanover Center	9617416218
5	Izio	42 Gateway Place	1051742437
6	Wordtune	0 Blaine Road	8713539566
7	Oloo	32 Lawn Pass	8134640718
8	Yoveo	294 Transport Court	9211843181
9	Trupe	362 Larry Way	7562659819
10	Oba	55603 Artisan Road	2936609196
\.


--
-- Name: company_company_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.company_company_id_seq', 10, true);


--
-- Data for Name: creditcard; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.creditcard (creditcard_id, payment_id, creditcard_name, creditcard_number, creditcard_ccv, creditcard_exp_date) FROM stdin;
1	11	Annecorinne Grioli	3547630567060007	580	11/21
3	13	Carlina Lentsch	3578439412600351	107	07/22
4	14	Marje Levine	3535932538008493	933	04/22
5	15	Roanna Curr	3557224543617283	543	12/21
6	16	Drugi Triebner	3530409392405045	202	06/22
7	17	Shanda Mapstone	3553561033882529	960	12/22
8	18	Rodi Cotte	3544975374249878	541	04/23
9	19	Cyndia Dullard	3566577009904324	312	06/21
10	20	Dieter Woodall	3581760837763671	730	05/23
2	12	Gene Chittey	3578891823683212	040	06/23
\.


--
-- Name: creditcard_creditcard_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.creditcard_creditcard_id_seq', 10, true);


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.customer (customer_id, user_id) FROM stdin;
1	31
2	32
3	33
4	34
5	35
6	36
7	37
8	38
9	39
10	40
11	41
12	42
13	43
14	44
15	45
16	46
17	47
18	48
19	49
20	50
21	51
22	52
23	53
24	54
25	55
26	56
27	57
28	58
29	59
30	60
\.


--
-- Name: customer_customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.customer_customer_id_seq', 30, true);


--
-- Data for Name: food; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.food (food_id, resource_id, food_category, food_container, food_type, food_expdate, food_ounces) FROM stdin;
1	51	dairy	metal	canned	02/04/2020	12
2	52	fruit	metal	canned	04/01/2020	16.100000000000001
3	53	vegetable	glass	baby	02/18/2020	4.5999999999999996
4	54	protein	glass	baby	01/10/2020	8
5	55	grains	plastic	dry	02/24/2020	24
6	56	protein	metal	canned	02/21/2020	12
7	57	grains	metal	canned	04/01/2020	16.100000000000001
8	58	dairy	plastic	dry	02/18/2020	4.5999999999999996
9	59	fruit	glass	baby	01/10/2020	8
10	60	protein	metal	canned	02/24/2020	16
\.


--
-- Name: food_food_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.food_food_id_seq', 10, true);


--
-- Data for Name: fuel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.fuel (fuel_id, resource_id, fuel_type, fuel_gallons) FROM stdin;
1	41	gasoline	6.2800000000000002
2	42	diesel	37.270000000000003
3	43	propane	40
4	44	gasoline	10.5
5	45	diesel	15.25
6	46	propane	15
7	47	gasoline	12.449999999999999
8	48	propane	25
9	49	diesel	35
10	50	gasoline	12.25
\.


--
-- Name: fuel_fuel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.fuel_fuel_id_seq', 10, true);


--
-- Data for Name: generators; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.generators (generator_id, resource_id, power_capacity, power_condition, generator_fuel) FROM stdin;
1	91	7000	Damaged	gasoline
2	92	7000	New	gas
3	93	5000	Damaged	diesel
4	94	24000	Used	gasoline
5	95	7500	Damaged	gas
6	96	6500	Used	gasoline
7	97	12000	Damaged	gas
8	98	5000	New	gasoline
9	99	5000	Used	gas
10	100	7000	New	gas
\.


--
-- Name: generators_generator_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.generators_generator_id_seq', 10, true);


--
-- Data for Name: heavy_equipment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.heavy_equipment (heavyequip_id, resource_id, heavyequip_type, heavyequip_model, heavyequip_condition) FROM stdin;
1	11	Excavator	320D	New
2	12	Motor Grader	12	Used
3	13	Yarders	325B	Used
4	14	Track Log Loaders	324D	Used
5	15	Track Log Loaders	2054	Used
6	16	Wheel Processor	1270D	Used
7	17	Skidders	525D	New
8	18	Towable Wood Chippers	90XP	Used
9	19	Towable Wood Chippers	CR70	Used
10	20	Excavator	320D	Used
\.


--
-- Name: heavy_equipment_heavyequip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.heavy_equipment_heavyequip_id_seq', 10, true);


--
-- Data for Name: ice; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ice (ice_id, resource_id, ice_weight) FROM stdin;
1	101	5
2	102	25
3	103	25
4	104	5
5	105	15
6	106	15
7	107	15
8	108	10
9	109	20
10	110	15
\.


--
-- Name: ice_ice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ice_ice_id_seq', 10, true);


--
-- Data for Name: login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.login (login_id, username, password, user_id) FROM stdin;
1	pgingles0	KkAUKm	1
2	ktoft1	re9vROF	2
3	sgaishson2	x6o7r4c28Xo	3
4	bgodsafe3	DwxnUWukqFb	4
5	jklulicek4	DeZSmiCZ0	5
6	jdebrick5	jJHxRtw	6
7	qhildred6	mbmkkgLegyjk	7
8	oatty7	YfLWLQDCa0y	8
9	ffaccini8	nRUonO	9
10	iaubrey9	0vrmQnu8n	10
11	cdobiea	V9Sa5g1QMCoA	11
12	hosgodbyb	Mhu3e8X	12
13	mheasemanc	K68HBsP9ybN	13
14	cgarrisond	YeBwYAIqQKBt	14
15	aelliffe	FRdLllDHi	15
16	rcalleyf	WMu6Q4if	16
17	bewdaleg	FJgbKn6TY2	17
18	dokeshotth	2r4Zvz	18
19	tlemonnieri	7TLsVZ	19
20	aannesj	Pai7FuH1j	20
21	hdomonkosk	TlPxSvo3yR	21
22	cgirvinl	iL37G9631	22
23	smagsonm	FPZLgkrN	23
24	nlashamn	xQgXCmF	24
25	cpenretho	fHduVEQLaB	25
26	gdowtyp	n1UZlg8	26
27	dgotliffeq	cvUqQCJ	27
28	gfilesr	rmOZzaJd	28
29	istablers	EUcZIi	29
30	rrumint	J0rovJaE21Ab	30
31	emegarrellu	wyRprSajl	31
32	mmcvaughv	ZSIl86MQKLch	32
33	tluxfordw	HqBAzjO4ZS	33
34	vbonifacex	xVy3vqK	34
35	aprestidgey	hDwV6CmA9Vz	35
36	mhallickz	E9TpNo	36
37	brennick10	79BG6Zn	37
38	ohavile11	EroFa7ugW	38
39	slorden12	SocCPboHUsHZ	39
40	nezzle13	dztRAYg0m	40
41	scaze14	mzSYlPDbvJEd	41
42	cedridge15	kHA1I4wqQFN	42
43	mmeneghi16	ECa66pjG	43
44	ulongforth17	zwcAhqjOJ	44
45	cmarnes18	bjPLQf	45
46	pvial19	DiQDgu3l	46
47	mschust1a	MZg6ymEyMK	47
48	kweavill1b	epjRj3	48
49	dwhitmarsh1c	53wIe2HB	49
50	lcausley1d	JmdfieMr3N	50
51	lcloake1e	z8cdYDsNPWve	51
52	amoynihan1f	jP4zdtDU	52
53	gfuzzens1g	Ux1287b0	53
54	habdy1h	eZSLpd9Vp	54
55	nlondors1i	nwAZgmY5RVz	55
56	aridgwell1j	2BRKQH0Dni	56
57	ksedgman1k	NkU63K5E5C3	57
58	kshuter1l	kdpmi8hPot3Y	58
59	hpopescu1m	gPpLZAshNGK	59
60	bcowx1n	F6bAIfOs9d	60
61	sflintiff1o	sAub2YSc	61
62	bcurrum1p	1Mkyg3x21z	62
63	mkerwick1q	MrPlz9	63
64	uolivelli1r	GJTVuCS7	64
65	tlivings1s	qr5WMG	65
66	ehearne1t	TJUFpUj7Dz	66
67	pjoyner1u	sqap0xcY	67
68	swerny1v	SW7AWO	68
69	dbacken1w	rn6euic	69
70	ylates1x	59jqjA	70
\.


--
-- Name: login_login_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.login_login_id_seq', 70, true);


--
-- Data for Name: manages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.manages (user_id, admin_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
\.


--
-- Data for Name: medical_device; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medical_device (med_device_id, resource_id, med_device_type, med_device_model, med_device_condition, med_device_power_type) FROM stdin;
1	21	Monitor glycemic control	A1C	New	Batteries
2	22	Pivot	13000	New	N/A
3	23	Transfer Bench	rtl12075	New	N/A
4	24	Walker	N/A	New	N/A
5	25	Walker	N/A	Used	N/A
6	26	Walker	796	New	Batteries
7	27	Pressure Monitor	Auto Arm	New	Batteries
8	28	Pressure Monitor	Auto Arm	Used	Batteries
9	29	Monitor glycemic control	A1C	Used	Batteries
10	30	Monitor glycemic control	A1C	Used	Batteries
\.


--
-- Name: medical_device_med_device_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medical_device_med_device_id_seq', 10, true);


--
-- Data for Name: medicine; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.medicine (med_id, resource_id, med_type, med_dose, med_prescript, med_expdate) FROM stdin;
1	61	allergy	25mg	N	03/14/2020
2	62	decongestant	30mg	N	04/24/2020
3	63	allergy	10mg	N	04/03/2020
4	64	migraine	50mg	Y	04/03/2020
5	65	pain	220mg	N	04/10/2020
6	66	fever	500mg	N	03/14/2020
7	67	eyes	0.28fl-oz	N	04/24/2020
8	68	diarrhea	262mg	N	04/03/2020
9	69	migraine	220mg	N	04/03/2020
10	70	pain	200mg	N	04/10/2020
\.


--
-- Name: medicine_med_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.medicine_med_id_seq', 10, true);


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.orders (order_id, customer_id, payment_id, order_date, order_price, order_status, request_id) FROM stdin;
1	1	1	01/23/2020	25.5	Accepted	\N
2	2	2	01/24/2020	30	Accepted	\N
3	3	3	01/25/2020	80100	Accepted	\N
4	4	4	01/23/2020	145	Accepted	\N
5	5	5	01/23/2020	25.5	Accepted	\N
6	6	6	01/23/2020	35	Accepted	\N
7	7	7	01/23/2020	80	Accepted	\N
8	8	8	01/23/2020	50	Accepted	\N
9	9	9	01/23/2020	2040	Accepted	\N
10	10	10	01/23/2020	85	Accepted	\N
\.


--
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 10, true);


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.payment (payment_id, customer_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
11	11
12	12
13	13
14	14
15	15
16	16
17	17
18	18
19	19
20	20
21	21
22	22
23	23
24	24
25	25
26	26
27	27
28	28
29	29
30	30
\.


--
-- Name: payment_payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payment_payment_id_seq', 30, true);


--
-- Data for Name: paypal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paypal (paypal_id, payment_id, paypal_username, paypal_password) FROM stdin;
1	21	ReynoldMc	Reynold1234
2	22	AbagailTri	Abagail1234
3	23	BarnabeStoll	Barnabe1234
4	24	Florette	Florette1234
5	25	TrynorMar	MartinTry1234
6	26	CathrynMc	Cathryn1234
7	27	RochellLucks	RochelLu1234
8	28	RhodieCat	RhodieCat1234
9	29	GillieCorn	CornwellGi1234
10	30	Eydie	Ludford1234
\.


--
-- Name: paypal_paypal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paypal_paypal_id_seq', 10, true);


--
-- Data for Name: represents; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.represents (company_id, supplier_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
\.


--
-- Data for Name: request; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.request (request_id, customer_id, request_title, request_date, request_description, request_status) FROM stdin;
1	1	Need Water and Men Cloth	05/01/2020	I need water and cloth in this emergency. I prefer t-shits for men and water in bottle.	Pending
2	2	Need Water	05/01/2020	I need water in bottle.	Pending
3	3	Need Good Generator	05/01/2020	I need a generator in good condition.	Pending
4	4	Need Fuel	05/01/2020	I need 5 gallons of fuel.	Pending
5	5	Need few Resources	05/01/2020	I need 10 boxes of water, 2 gallons of fuel, 1 generator, medicine, and cloth.	Pending
6	6	Need Water ASAP	05/02/2020	I need water in bottle.	Pending
7	7	Need Kids Cloth	05/02/2020	I need cloth for kids.	Pending
8	8	Need Food	05/02/2020	I need canned food.	Pending
9	9	Need Ice	05/02/2020	I need 10 bags of ice.	Pending
10	10	Need Batteries	05/02/2020	I need batteries.	Pending
\.


--
-- Data for Name: request_category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.request_category (request_id, category_id, request_quantity) FROM stdin;
1	7	15
1	5	5
2	7	20
3	10	1
4	1	5
5	7	10
5	1	2
5	10	1
5	5	10
6	7	40
7	5	10
8	2	25
9	11	10
10	9	20
\.


--
-- Name: request_request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.request_request_id_seq', 10, true);


--
-- Data for Name: reservation; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reservation (reservation_id, customer_id, reservation_date, reservation_status, request_id) FROM stdin;
1	1	01/23/2020	Accepted	\N
2	2	04/25/2020	Pending	\N
3	3	03/04/2020	Accepted	\N
4	4	05/02/2020	Pending	4
5	5	03/05/2020	Accepted	\N
6	6	05/03/2020	Pending	\N
7	7	03/16/2020	Accepted	\N
8	8	05/02/2020	Pending	8
9	9	05/02/2020	Pending	\N
10	10	03/05/2020	Accepted	\N
\.


--
-- Name: reservation_reservation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reservation_reservation_id_seq', 10, true);


--
-- Data for Name: resource; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resource (resource_id, supplier_id, category_id, resource_name, resource_brand, resource_quantity, resource_price) FROM stdin;
1	1	5	T-shirt	Aeropostal	50	20
2	2	5	T-shirt	Puma	60	22
3	3	5	Pants	Old Navy	30	10
4	4	5	T-shirt	Aeropostal	50	20
5	5	5	Shoes	Puma	10	16
6	6	5	Polo	Aeropostal	20	20
7	7	5	Pants	Adidas	70	24
8	8	5	T-shirt	Nike	80	27
9	9	5	Sweater	Gap	50	26
10	10	5	Infant Girl	Carter	35	10
11	11	6	Caterpillar Excavator	Caterpillar	2	130000
12	12	6	1996 Cat 12	Caterpillar	1	5000
13	13	6	2001 Cat 325B	Caterpillar	1	150000
14	14	6	2013 Cat 324D FM	Caterpillar	2	120000
15	15	6	2006 Deere 2054	Deere	1	100000
16	16	6	2006 Deere 1270D	Deere	1	110000
17	17	6	Caterpillar Skidders	Caterpillar	2	150000
18	18	6	Bandit 90XP	Bandit	3	80000
19	19	6	2017 Wallenstein CR70	Wallenstein	2	100000
20	20	6	Caterpillar Excavator 320D	Caterpillar	2	110000
21	1	8	Walgreens At-Home A1C Test Kit	Walgreens	2	45
22	2	8	Drive Medical Pivot	Walgreens	2	82
23	3	8	Drive Medical Folding	Walgreens	2	140
24	4	8	Lumex Adult Folding Walker	Lumex	1	30
25	5	8	Lumex Walker	Lumex	1	20
26	6	8	Driver Medical Dual Pad	Lumex	1	130
27	7	8	Auto Arm Blood Pressure Monitor	Walgreens	5	40
28	8	8	Pressure Monitor	Walgreens	2	30
29	9	8	At-Home A1C Test Kit	Walgreens	1	30
30	10	8	A1C Test Kit	Walgreens	2	28
31	21	7	Water Vita	Vita	24	1
32	22	7	Box Water Vita	Vita	10	20
33	23	7	Water Great Value	Great Value	32	1
34	24	7	Water Dasani	Dasani	50	22
35	25	7	Water Aquafina	Aquafina	100	3
36	26	7	Water Vita	Vita	50	5
37	27	7	Water Fiji	Fiji	30	1
38	28	7	Water Vita	Vita	24	1
39	29	7	Water Evian	Evian	24	1
40	30	7	Water Smartwater	Smartwater	10	0.80000000000000004
41	1	1	Gasoline	Shell	5	30.5
42	2	1	Diesel	Exxon Mobil	2	70.980000000000004
43	3	1	Propane	AMERIGAS	1	65
44	4	1	Gasoline	Chevron	3	25.649999999999999
45	5	1	Diesel	Shell	1	31.5
46	6	1	Propane	Empire Gas	10	0
47	7	1	Gasoline	Total	10	0
48	8	1	Propane	Empire Gas	1	20
49	9	1	Diesel	Chevron	3	20.5
50	10	1	Gasoline	Shell	1	0
51	1	2	Evaporated milk	Indulac	6	0
52	2	2	Canned peaches	Del Monte	12	0
53	3	2	Carrot baby food	Gerber	24	5
54	4	2	Beans baby food	Gerber	30	12
55	5	2	Bread	Pan Pepin	10	0
56	6	2	Canned chicken breast	Kirkland	12	0
57	7	2	Mixed nuts	Great Value	3	2
58	8	2	Cheese sticks	Borden	10	5
59	9	2	Banana baby food	Gerber	15	0
60	10	2	Corned beef	Great Value	20	5
61	1	3	Benadryl	Benadryl	24	0
62	2	3	Zyrtec	Zyrtec	2	10
63	3	3	Claritin	Claritin	5	5
64	4	3	Sumatriptan	Walgreens	1	0
65	5	3	Aleve	Aleve	6	0
66	6	3	Tylenol	Tylenol	5	5
67	7	3	Eye drops	Visine	2	6
68	8	3	Pepto Bismol chewables	Pepto Bismol	5	0
69	9	3	Excedrin Migraine	Excedrin	4	6.4900000000000002
70	10	3	Ibuprofen	Equate	1	2
71	1	4	Multimeter	Extech	1	35.890000000000001
72	2	4	Adjustable wrench	Craftsman	2	25.890000000000001
73	3	4	Stepladder	Werner	1	37.990000000000002
74	4	4	Power drill	Ryobi	1	39.969999999999999
75	5	4	All-purpose hammer	Craftsman	1	0
76	6	4	Tape measure	Stanley	1	0
77	7	4	Pry bar (12 in.)	Stanley	2	16.98
78	8	4	Retractable utility knife	Dewalt	2	9.9800000000000004
79	9	4	Cordless high pressure inflator	Ryobi	1	24.969999999999999
80	10	4	Screwdriver set	Milwaukee	1	0
81	1	9	Battery	Energizer	32	116.93000000000001
82	2	9	Battery	Eveready	95	113.56
83	3	9	Battery	Eveready	14	26.510000000000002
84	4	9	Battery	Panasonic	99	40.25
85	5	9	Battery	Rayovac	94	27.989999999999998
86	6	9	Battery	Energizer	32	67.409999999999997
87	7	9	Battery	Duracell	18	9.1400000000000006
88	8	9	Battery	Panasonic	79	28.300000000000001
89	9	9	Battery	Duracell	87	151.81999999999999
90	10	9	Battery	Duracell	80	87.010000000000005
91	1	10	Generator	Generac	20	2753.1900000000001
92	2	10	Generator	Westinghouse	35	2025.05
93	3	10	Generator	Winco	9	2065.3200000000002
94	4	10	Generator	Energizer	36	2702.7800000000002
95	5	10	Generator	Energizer	41	2569.1300000000001
96	6	10	Generator	Honda	11	497.12
97	7	10	Generator	Westinghouse	22	1433.4200000000001
98	8	10	Generator	Energizer	9	917.94000000000005
99	9	10	Generator	Westinghouse	19	2740.5300000000002
100	10	10	Generator	Honda	50	1349.1800000000001
101	1	11	Ice	Crystal Lake Ice Company	32	24.649999999999999
102	2	11	Ice	Barton	85	23.59
103	3	11	Ice	Lowell	12	21.699999999999999
104	4	11	Ice	Vermont Crystal Lake Ice Company	61	23.379999999999999
105	5	11	Ice	Illinois Crystal Lake Ice Company	26	19.530000000000001
106	6	11	Ice	Massachusetts Crystal Lake Ice Company	38	12.74
107	7	11	Ice	Crystal Lake Ice Company	50	22.530000000000001
108	8	11	Ice	Minnesota	13	24.030000000000001
109	9	11	Ice	Vermont Crystal Lake Ice Company	22	7.9199999999999999
110	10	11	Ice	Crystal Lake Ice Company	65	19.75
\.


--
-- Data for Name: resource_orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resource_orders (order_id, resource_id, discount, order_quantity) FROM stdin;
1	49	0.20000000000000001	1
1	53	0.20000000000000001	5
2	1	0.20000000000000001	1
2	3	0.20000000000000001	5
3	18	0.29999999999999999	1
3	5	0.20000000000000001	5
4	26	0.20000000000000001	1
4	35	0.20000000000000001	5
5	49	0.20000000000000001	1
5	53	0.20000000000000001	5
6	28	0.20000000000000001	1
6	37	0.20000000000000001	5
7	60	0.20000000000000001	1
7	101	0.20000000000000001	5
8	77	0.20000000000000001	1
8	109	0.20000000000000001	5
9	45	0.20000000000000001	1
9	92	0.20000000000000001	5
10	22	0.20000000000000001	1
10	88	0.20000000000000001	5
\.


--
-- Data for Name: resource_reservations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.resource_reservations (reservation_id, resource_id, reservation_quantity) FROM stdin;
1	50	1
1	51	5
2	55	3
2	46	5
3	80	1
3	59	10
4	47	1
5	75	1
6	61	12
7	76	1
8	56	10
8	52	6
9	55	2
9	47	3
10	65	2
10	64	1
10	68	5
\.


--
-- Name: resource_resource_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.resource_resource_id_seq', 110, true);


--
-- Data for Name: supplier; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.supplier (supplier_id, user_id) FROM stdin;
1	1
2	2
3	3
4	4
5	5
6	6
7	7
8	8
9	9
10	10
11	11
12	12
13	13
14	14
15	15
16	16
17	17
18	18
19	19
20	20
21	21
22	22
23	23
24	24
25	25
26	26
27	27
28	28
29	29
30	30
\.


--
-- Name: supplier_supplier_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.supplier_supplier_id_seq', 30, true);


--
-- Data for Name: tools; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tools (tool_id, resource_id, tool_material, tool_condition, tool_pwtype) FROM stdin;
1	71	plastic	used	battery
2	72	steel alloy	new	N/A
3	73	fiberglass	new	N/A
4	74	steel	used	AC voltage
5	75	steel	like new	N/A
6	76	metal	used	N/A
7	77	stainless steel	like new	N/A
8	78	steel alloy	new	N/A
9	79	plastic	like new	DC voltage
10	80	stainless steel	used	N/A
\.


--
-- Name: tools_tool_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tools_tool_id_seq', 10, true);


--
-- Data for Name: user_phone; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_phone (phone_id, user_id, user_phone) FROM stdin;
1	1	3159711232
2	2	5021230956
3	3	1110074567
4	4	5034530967
5	5	5031112122
6	6	5030542671
7	7	5032331100
8	8	5033335436
9	9	5036759041
10	10	5038097600
11	11	8263931430
12	12	6785896715
13	13	4486375911
14	14	8697779210
15	15	7422347924
16	16	1219678406
17	17	5675723102
18	18	4491081002
19	19	1668066817
20	20	2893367349
21	21	9554051438
22	22	7196141340
23	23	3349443538
24	24	6859526819
25	25	9285060971
26	26	3036461920
27	27	2334617615
28	28	7428817700
29	29	7992726804
30	30	9277701357
31	31	3154554321
32	32	3150901154
33	33	3157960978
34	34	3159159151
35	35	3151060294
36	36	3159944952
37	37	3150005412
38	38	5040943184
39	39	3165673214
40	40	3167891234
41	41	2891552184
42	42	1525619800
43	43	1886901864
44	44	4425115108
45	45	8077286723
46	46	6988408470
47	47	9025671208
48	48	4595855187
49	49	5816878538
50	50	9725988649
51	51	5687333172
52	52	1549964276
53	53	8027281957
54	54	1517659688
55	55	4518636414
56	56	8175520582
57	57	6261924677
58	58	9724020442
59	59	6828459956
60	60	3904115563
61	61	9594001344
62	62	2301506825
63	63	3144236123
64	64	8908771897
65	65	2676485525
66	66	6334782229
67	67	3022247898
68	68	3423136269
69	69	8439722037
70	70	5766614945
\.


--
-- Name: user_phone_phone_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_phone_phone_id_seq', 70, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, user_firstname, user_lastname, user_date_birth, user_email) FROM stdin;
1	Violet	Scarlet	06/28/1988	vscarlet@gm.com
2	Miguel	Martinez	08/20/1990	miguelitomartinez1@gm.com
3	Samanta	Zamora	02/16/1991	samzamora23@gm.com
4	Kaleb	Rios	05/05/1989	kaleb34@gm.com
5	Jasmine	Ortiz	05/05/1989	jasmineortiz12@gm.com
6	Minerva	Hernandez	01/14/1985	minervaher08@gm.com
7	Pablo	Diaz	11/22/1992	pablitodiaz45@gm.com
8	Javier	Perez	09/21/1994	javiperez56@gm.com
9	Alex	Scarlet	03/08/1991	alexscarlet@gm.com
10	Sammy	Jimenez	12/08/1987	sammyjimenez@gm.com
11	Lucila	Antonsen	10/14/1991	lantonsen0@nydailynews.com
12	Barb	Clawsley	02/08/1980	bclawsley1@businessweek.com
13	Turner	Sabates	01/03/1997	tsabates2@livejournal.com
14	Cece	O'Driscole	02/26/1994	codriscole3@example.com
15	Georas	Littell	04/05/1997	glittell4@hexun.com
16	Kyla	Ravelus	11/06/1987	kravelus5@uol.com.br
17	Elfrida	Dreier	09/23/1988	edreier6@boston.com
18	Sandro	Wolfenden	07/14/1994	swolfenden7@japanpost.jp
19	Enrichetta	Abbyss	12/01/1984	eabbyss8@theguardian.com
20	Aile	Scales	10/15/1980	ascales9@google.ca
21	Amalee	Vinnicombe	11/20/1985	avinnicombea@flavors.me
22	Ash	Badham	06/07/1993	abadhamb@virginia.edu
23	Bibbye	Stirrup	08/22/1994	bstirrupc@csmonitor.com
24	Elysha	Birdsall	12/09/1999	ebirdsalld@last.fm
25	Domini	Rosenstein	02/17/1995	drosensteine@skype.com
26	Mureil	Vigus	08/07/1998	mvigusf@hatena.ne.jp
27	Reinhard	Fairbeard	10/08/1981	rfairbeardg@ask.com
28	Kala	Prentice	09/12/1987	kprenticeh@abc.net.au
29	Livvyy	Fedorski	11/21/1987	lfedorskii@hao123.com
30	Waverley	Dotson	03/23/1989	wdotsonj@ifeng.com
31	Felix	Scarlet	03/25/1986	fscarlet@gm.com
32	Elmer	Zacarias	07/25/1988	elmzacarias@gm.com
33	Graciela	Ocasio	06/29/1993	gocasio@gm.com
34	Karelis	Alvarez	01/28/1990	akarelis@gm.com
35	Klaus	Espinoza	10/25/1991	klausnoza@gm.com
36	Lorena	Cabales	03/25/1986	lorenacabales5@gm.com
37	Xavier	Moreno	02/25/1986	xaviermoreno9@gm.com
38	Liliana	Lopez	07/25/1995	lililopez@gm.com
39	David	Velez	09/01/1996	davidvelez43@gm.com
40	Danna	Gracia	04/10/1992	dannagracia@gm.com
41	Annecorinne	Grioli	02/05/1994	agrioli0@reverbnation.com
42	Gene	Chittey	07/17/1991	gchittey1@behance.net
43	Carlina	Lentsch	11/27/2000	clentsch2@nymag.com
44	Marje	Levine	04/17/1994	mlevine3@uol.com.br
45	Roanna	Curr	01/04/1999	rcurr4@dot.gov
46	Drugi	Triebner	11/11/1982	dtriebner5@unicef.org
47	Shanda	Mapstone	07/15/1994	smapstone6@surveymonkey.com
48	Rodi	Cotte	07/03/1992	rcotte7@telegraph.co.uk
49	Cyndia	Dullard	06/19/1996	cdullard8@geocities.jp
50	Dieter	Woodall	10/05/1999	dwoodall9@odnoklassniki.ru
51	Reynold	McRae	07/25/1980	rmcraea@ftc.gov
52	Abagail	Tripon	03/17/1982	atriponb@alibaba.com
53	Barnabe	Stoll	11/25/1994	bstollc@pen.io
54	Florette	Agass	06/02/1987	fagassd@t.co
55	Martin	Trynor	08/19/1992	mtrynore@prweb.com
56	Cathryn	MacRonald	10/25/1998	cmacronaldf@vk.com
57	Rochell	Lucks	07/29/1987	rlucksg@reverbnation.com
58	Rhodie	Catterson	10/18/1991	rcattersonh@vk.com
59	Gillie	Cornwell	09/13/1997	gcornwelli@hatena.ne.jp
60	Eydie	Ludford	10/18/1997	eludfordj@imdb.com
61	Mechelle	Tebbe	12/20/2009	mtebbe0@1688.com
62	Davita	Crowdson	02/20/1990	dcrowdson1@vinaora.com
63	Averil	Nolte	07/14/1980	anolte2@weibo.com
64	Pearline	Berendsen	07/27/1999	pberendsen3@epa.gov
65	Rubi	Grills	09/07/1992	rgrills4@mtv.com
66	Mohammed	Bouchard	01/25/1998	mbouchard5@businesswire.com
67	Kinsley	Seath	03/16/1988	kseath6@theatlantic.com
68	Ardelis	Lening	06/23/1997	alening7@webs.com
69	Ealasaid	Beyer	07/02/1995	ebeyer8@addthis.com
70	Aveline	Christol	01/21/1994	achristol9@myspace.com
\.


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_user_id_seq', 70, true);


--
-- Data for Name: water; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.water (water_id, resource_id, water_size, water_container, water_type, water_exp_date) FROM stdin;
1	31	16oz	Bottle	Purified	02/02/2022
2	32	16oz	Box	Purified	02/10/2022
3	33	8oz	Bottle	Purified	02/02/2023
4	34	16oz	Bottle	Purified	08/10/2024
5	35	1 gallon	Gallon	Purified	02/02/2025
6	36	1 gallon	Gallon	Purified	12/02/2024
7	37	16oz	Bottle	Purified	02/02/2022
8	38	16oz	Bottle	Purified	02/02/2022
9	39	16oz	Bottle	Purified	02/02/2022
10	40	16oz	Bottle	Purified	02/02/2026
\.


--
-- Name: water_water_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.water_water_id_seq', 10, true);


--
-- Name: address address_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_pkey PRIMARY KEY (address_id);


--
-- Name: admin admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_pkey PRIMARY KEY (admin_id);


--
-- Name: ath_movil ath_movil_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ath_movil
    ADD CONSTRAINT ath_movil_pkey PRIMARY KEY (ath_movil_id);


--
-- Name: batteries batteries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.batteries
    ADD CONSTRAINT batteries_pkey PRIMARY KEY (battery_id);


--
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (category_id);


--
-- Name: cloth cloth_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cloth
    ADD CONSTRAINT cloth_pkey PRIMARY KEY (cloth_id);


--
-- Name: company company_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (company_id);


--
-- Name: creditcard creditcard_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.creditcard
    ADD CONSTRAINT creditcard_pkey PRIMARY KEY (creditcard_id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_id);


--
-- Name: food food_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_pkey PRIMARY KEY (food_id);


--
-- Name: fuel fuel_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fuel
    ADD CONSTRAINT fuel_pkey PRIMARY KEY (fuel_id);


--
-- Name: generators generators_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generators
    ADD CONSTRAINT generators_pkey PRIMARY KEY (generator_id);


--
-- Name: heavy_equipment heavy_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heavy_equipment
    ADD CONSTRAINT heavy_equipment_pkey PRIMARY KEY (heavyequip_id);


--
-- Name: ice ice_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ice
    ADD CONSTRAINT ice_pkey PRIMARY KEY (ice_id);


--
-- Name: login login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_pkey PRIMARY KEY (login_id);


--
-- Name: manages manages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_pkey PRIMARY KEY (user_id, admin_id);


--
-- Name: medical_device medical_device_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_device
    ADD CONSTRAINT medical_device_pkey PRIMARY KEY (med_device_id);


--
-- Name: medicine medicine_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT medicine_pkey PRIMARY KEY (med_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- Name: payment payment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pkey PRIMARY KEY (payment_id);


--
-- Name: paypal paypal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paypal
    ADD CONSTRAINT paypal_pkey PRIMARY KEY (paypal_id);


--
-- Name: represents represents_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.represents
    ADD CONSTRAINT represents_pkey PRIMARY KEY (company_id, supplier_id);


--
-- Name: request_category request_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request_category
    ADD CONSTRAINT request_category_pkey PRIMARY KEY (request_id, category_id);


--
-- Name: request request_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_pkey PRIMARY KEY (request_id);


--
-- Name: reservation reservation_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (reservation_id);


--
-- Name: resource_orders resource_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_orders
    ADD CONSTRAINT resource_orders_pkey PRIMARY KEY (order_id, resource_id);


--
-- Name: resource resource_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource
    ADD CONSTRAINT resource_pkey PRIMARY KEY (resource_id);


--
-- Name: resource_reservations resource_reservations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_reservations
    ADD CONSTRAINT resource_reservations_pkey PRIMARY KEY (reservation_id, resource_id);


--
-- Name: supplier supplier_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_pkey PRIMARY KEY (supplier_id);


--
-- Name: tools tools_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tools
    ADD CONSTRAINT tools_pkey PRIMARY KEY (tool_id);


--
-- Name: user_phone user_phone_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_phone
    ADD CONSTRAINT user_phone_pkey PRIMARY KEY (phone_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: water water_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_pkey PRIMARY KEY (water_id);


--
-- Name: address address_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.address
    ADD CONSTRAINT address_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: admin admin_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.admin
    ADD CONSTRAINT admin_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: ath_movil ath_movil_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ath_movil
    ADD CONSTRAINT ath_movil_payment_id_fkey FOREIGN KEY (payment_id) REFERENCES public.payment(payment_id);


--
-- Name: batteries batteries_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.batteries
    ADD CONSTRAINT batteries_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: cloth cloth_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cloth
    ADD CONSTRAINT cloth_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: creditcard creditcard_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.creditcard
    ADD CONSTRAINT creditcard_payment_id_fkey FOREIGN KEY (payment_id) REFERENCES public.payment(payment_id);


--
-- Name: customer customer_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: food food_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.food
    ADD CONSTRAINT food_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: fuel fuel_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.fuel
    ADD CONSTRAINT fuel_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: generators generators_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.generators
    ADD CONSTRAINT generators_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: heavy_equipment heavy_equipment_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.heavy_equipment
    ADD CONSTRAINT heavy_equipment_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: ice ice_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ice
    ADD CONSTRAINT ice_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: login login_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.login
    ADD CONSTRAINT login_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: manages manages_admin_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_admin_id_fkey FOREIGN KEY (admin_id) REFERENCES public.admin(admin_id);


--
-- Name: manages manages_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.manages
    ADD CONSTRAINT manages_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: medical_device medical_device_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medical_device
    ADD CONSTRAINT medical_device_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: medicine medicine_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.medicine
    ADD CONSTRAINT medicine_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: orders orders_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- Name: orders orders_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_payment_id_fkey FOREIGN KEY (payment_id) REFERENCES public.payment(payment_id);


--
-- Name: orders orders_request_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_request_id_fkey FOREIGN KEY (request_id) REFERENCES public.request(request_id);


--
-- Name: payment payment_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- Name: paypal paypal_payment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paypal
    ADD CONSTRAINT paypal_payment_id_fkey FOREIGN KEY (payment_id) REFERENCES public.payment(payment_id);


--
-- Name: represents represents_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.represents
    ADD CONSTRAINT represents_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.company(company_id);


--
-- Name: represents represents_supplier_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.represents
    ADD CONSTRAINT represents_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES public.supplier(supplier_id);


--
-- Name: request_category request_category_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request_category
    ADD CONSTRAINT request_category_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(category_id);


--
-- Name: request_category request_category_request_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request_category
    ADD CONSTRAINT request_category_request_id_fkey FOREIGN KEY (request_id) REFERENCES public.request(request_id);


--
-- Name: request request_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.request
    ADD CONSTRAINT request_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- Name: reservation reservation_customer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_customer_id_fkey FOREIGN KEY (customer_id) REFERENCES public.customer(customer_id);


--
-- Name: reservation reservation_request_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reservation
    ADD CONSTRAINT reservation_request_id_fkey FOREIGN KEY (request_id) REFERENCES public.request(request_id);


--
-- Name: resource resource_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource
    ADD CONSTRAINT resource_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.category(category_id);


--
-- Name: resource_orders resource_orders_order_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_orders
    ADD CONSTRAINT resource_orders_order_id_fkey FOREIGN KEY (order_id) REFERENCES public.orders(order_id);


--
-- Name: resource_orders resource_orders_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_orders
    ADD CONSTRAINT resource_orders_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: resource_reservations resource_reservations_reservation_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_reservations
    ADD CONSTRAINT resource_reservations_reservation_id_fkey FOREIGN KEY (reservation_id) REFERENCES public.reservation(reservation_id);


--
-- Name: resource_reservations resource_reservations_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource_reservations
    ADD CONSTRAINT resource_reservations_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: resource resource_supplier_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.resource
    ADD CONSTRAINT resource_supplier_id_fkey FOREIGN KEY (supplier_id) REFERENCES public.supplier(supplier_id);


--
-- Name: supplier supplier_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.supplier
    ADD CONSTRAINT supplier_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: tools tools_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tools
    ADD CONSTRAINT tools_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- Name: user_phone user_phone_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_phone
    ADD CONSTRAINT user_phone_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: water water_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.water
    ADD CONSTRAINT water_resource_id_fkey FOREIGN KEY (resource_id) REFERENCES public.resource(resource_id);


--
-- PostgreSQL database dump complete
--

