--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.5 (Ubuntu 12.5-0ubuntu0.20.04.1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: trips; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trips (
    traveller_id integer NOT NULL,
    venue_id integer NOT NULL
);


ALTER TABLE public.trips OWNER TO postgres;

--
-- Name: travellers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.travellers (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer NOT NULL,
    gender character varying NOT NULL,
    start timestamp without time zone
);


ALTER TABLE public.travellers OWNER TO postgres;

--
-- Name: travellers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.travellers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.travellers_id_seq OWNER TO postgres;

--
-- Name: travellers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.travellers_id_seq OWNED BY public.travellers.id;


--
-- Name: venues; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.venues (
    id integer NOT NULL,
    vname character varying NOT NULL,
    visit_year integer NOT NULL,
    duration integer NOT NULL,
    start timestamp without time zone
);


ALTER TABLE public.venues OWNER TO postgres;

--
-- Name: venues_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.venues_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.venues_id_seq OWNER TO postgres;

--
-- Name: venues_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.venues_id_seq OWNED BY public.venues.id;


--
-- Name: travellers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travellers ALTER COLUMN id SET DEFAULT nextval('public.travellers_id_seq'::regclass);


--
-- Name: venues id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venues ALTER COLUMN id SET DEFAULT nextval('public.venues_id_seq'::regclass);


--
-- Data for Name: trips; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trips (traveller_id, venue_id) FROM stdin;
\.


--
-- Data for Name: travellers; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.travellers (id, name, age, gender, start) FROM stdin;
1	Tommy	23	male	2020-04-11 18:49:18.770627
3	Rosemary	55	female	2021-03-18 18:50:05.344209
4	Willen	40	male	2021-03-18 18:50:22.707984
5	Robert	50	male	2021-03-18 19:26:34.497392
6	Chris Evans	40	male	2021-03-18 19:34:32.4428
7	Robert Downey	55	male	2021-03-18 19:34:49.393957
8	Jennifer Lawrence	30	female	2021-03-18 19:35:08.465082
9	Margot Robbie	30	female	2021-03-18 19:35:20.959215
10	Scarlett Johansson	37	female	2021-03-18 19:35:49.710734
11	Tom Holland	24	male	2021-03-18 19:39:27.059772
2	Megan Fox	32	female	2021-03-18 18:49:54.722849
\.


--
-- Data for Name: venues; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.venues (id, vname, visit_year, duration, start) FROM stdin;
2	spider man 3	2005	4	2021-03-18 18:47:11.754451
3	Titanic	1998	2	2021-03-18 18:47:23.52503
4	Avengers 1	2012	3	2021-03-18 19:38:01.822417
5	Avengers 2	2015	2	2021-03-18 19:38:21.917448
6	Rocky I	1976	2	2021-03-18 19:38:37.478519
8	La hera del hielo	2018	2	2021-03-18 21:50:36.242575
1	kong I	1976	2	2021-03-18 18:46:53.371192
\.


--
-- Name: travellers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.travellers_id_seq', 12, true);


--
-- Name: venues_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.venues_id_seq', 8, true);


--
-- Name: trips trips_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trips
    ADD CONSTRAINT trips_pkey PRIMARY KEY (traveller_id, venue_id);


--
-- Name: travellers travellers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travellers
    ADD CONSTRAINT travellers_pkey PRIMARY KEY (id);


--
-- Name: venues venues_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venues
    ADD CONSTRAINT venues_pkey PRIMARY KEY (id);


--
-- Name: trips trips_traveller_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trips
    ADD CONSTRAINT trips_traveller_id_fkey FOREIGN KEY (traveller_id) REFERENCES public.travellers(id);


--
-- Name: trips trips_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trips
    ADD CONSTRAINT trips_venue_id_fkey FOREIGN KEY (venue_id) REFERENCES public.venues(id);


--
-- PostgreSQL database dump complete
--

