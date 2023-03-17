--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

-- Started on 2022-06-27 20:22:49

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

DROP DATABASE local_mixing_process;
--
-- TOC entry 3375 (class 1262 OID 16394)
-- Name: local_mixing_process; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE local_mixing_process WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Mexico.1252';


ALTER DATABASE local_mixing_process OWNER TO postgres;

\connect local_mixing_process

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
-- TOC entry 221 (class 1259 OID 16461)
-- Name: MixContainer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."MixContainer" (
    id integer NOT NULL,
    id_barcode integer,
    id_process integer,
    viscosity double precision,
    t_start timestamp without time zone,
    t_end timestamp without time zone,
    t_end_tare timestamp without time zone,
    t_start_container timestamp without time zone,
    t_end_container timestamp without time zone,
    t_start_viscosity timestamp without time zone,
    t_end_viscosity timestamp without time zone
);


ALTER TABLE public."MixContainer" OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16460)
-- Name: MixContainer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."MixContainer_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."MixContainer_id_seq" OWNER TO postgres;

--
-- TOC entry 3376 (class 0 OID 0)
-- Dependencies: 220
-- Name: MixContainer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."MixContainer_id_seq" OWNED BY public."MixContainer".id;


--
-- TOC entry 217 (class 1259 OID 16437)
-- Name: componenttare; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.componenttare (
    id integer NOT NULL,
    id_mix_container integer NOT NULL,
    id_component integer NOT NULL,
    weight double precision,
    t_start timestamp without time zone NOT NULL,
    t_end timestamp without time zone
);


ALTER TABLE public.componenttare OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16436)
-- Name: componenttare_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.componenttare_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.componenttare_id_seq OWNER TO postgres;

--
-- TOC entry 3377 (class 0 OID 0)
-- Dependencies: 216
-- Name: componenttare_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.componenttare_id_seq OWNED BY public.componenttare.id;


--
-- TOC entry 219 (class 1259 OID 16449)
-- Name: componentviscosityimprovement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.componentviscosityimprovement (
    id integer NOT NULL,
    id_viscosity_improvement integer NOT NULL,
    id_component integer NOT NULL,
    extra_weight double precision,
    t_start timestamp without time zone NOT NULL,
    t_end timestamp without time zone
);


ALTER TABLE public.componentviscosityimprovement OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16448)
-- Name: componentviscosityimprovement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.componentviscosityimprovement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.componentviscosityimprovement_id_seq OWNER TO postgres;

--
-- TOC entry 3378 (class 0 OID 0)
-- Dependencies: 218
-- Name: componentviscosityimprovement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.componentviscosityimprovement_id_seq OWNED BY public.componentviscosityimprovement.id;


--
-- TOC entry 212 (class 1259 OID 16403)
-- Name: mixcontainer; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mixcontainer (
    id integer NOT NULL,
    id_barcode integer NOT NULL,
    id_process integer NOT NULL,
    viscosity double precision,
    t_start timestamp without time zone NOT NULL,
    t_end timestamp without time zone,
    t_end_tare timestamp without time zone,
    t_start_container timestamp without time zone,
    t_end_container timestamp without time zone,
    t_start_viscosity timestamp without time zone,
    t_end_viscosity timestamp without time zone
);


ALTER TABLE public.mixcontainer OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 16402)
-- Name: mixcontainer_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mixcontainer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mixcontainer_id_seq OWNER TO postgres;

--
-- TOC entry 3379 (class 0 OID 0)
-- Dependencies: 211
-- Name: mixcontainer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mixcontainer_id_seq OWNED BY public.mixcontainer.id;


--
-- TOC entry 210 (class 1259 OID 16396)
-- Name: mixingprocess; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mixingprocess (
    id integer NOT NULL,
    id_worker integer NOT NULL,
    name_worker character varying(64),
    id_formula integer NOT NULL,
    id_filter integer NOT NULL,
    num_containers integer NOT NULL,
    t_start timestamp without time zone,
    t_end timestamp without time zone,
    expected_viscosity_min double precision NOT NULL,
    expected_viscosity_max double precision NOT NULL
);


ALTER TABLE public.mixingprocess OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 16395)
-- Name: mixingprocess_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mixingprocess_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mixingprocess_id_seq OWNER TO postgres;

--
-- TOC entry 3380 (class 0 OID 0)
-- Dependencies: 209
-- Name: mixingprocess_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mixingprocess_id_seq OWNED BY public.mixingprocess.id;


--
-- TOC entry 215 (class 1259 OID 16426)
-- Name: processcontainercomponent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.processcontainercomponent (
    id_mix_container integer NOT NULL,
    id_component integer NOT NULL,
    weight double precision NOT NULL
);


ALTER TABLE public.processcontainercomponent OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16415)
-- Name: viscosityimprovement; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.viscosityimprovement (
    id integer NOT NULL,
    id_mix_container integer NOT NULL,
    new_viscosity double precision,
    extra_weight double precision,
    t_start timestamp without time zone NOT NULL,
    t_end timestamp without time zone
);


ALTER TABLE public.viscosityimprovement OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16414)
-- Name: viscosityimprovement_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.viscosityimprovement_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.viscosityimprovement_id_seq OWNER TO postgres;

--
-- TOC entry 3381 (class 0 OID 0)
-- Dependencies: 213
-- Name: viscosityimprovement_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.viscosityimprovement_id_seq OWNED BY public.viscosityimprovement.id;


--
-- TOC entry 3198 (class 2604 OID 16464)
-- Name: MixContainer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MixContainer" ALTER COLUMN id SET DEFAULT nextval('public."MixContainer_id_seq"'::regclass);


--
-- TOC entry 3196 (class 2604 OID 16440)
-- Name: componenttare id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componenttare ALTER COLUMN id SET DEFAULT nextval('public.componenttare_id_seq'::regclass);


--
-- TOC entry 3197 (class 2604 OID 16452)
-- Name: componentviscosityimprovement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componentviscosityimprovement ALTER COLUMN id SET DEFAULT nextval('public.componentviscosityimprovement_id_seq'::regclass);


--
-- TOC entry 3194 (class 2604 OID 16406)
-- Name: mixcontainer id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mixcontainer ALTER COLUMN id SET DEFAULT nextval('public.mixcontainer_id_seq'::regclass);


--
-- TOC entry 3193 (class 2604 OID 16399)
-- Name: mixingprocess id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mixingprocess ALTER COLUMN id SET DEFAULT nextval('public.mixingprocess_id_seq'::regclass);


--
-- TOC entry 3195 (class 2604 OID 16418)
-- Name: viscosityimprovement id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viscosityimprovement ALTER COLUMN id SET DEFAULT nextval('public.viscosityimprovement_id_seq'::regclass);


--
-- TOC entry 3369 (class 0 OID 16461)
-- Dependencies: 221
-- Data for Name: MixContainer; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3365 (class 0 OID 16437)
-- Dependencies: 217
-- Data for Name: componenttare; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3367 (class 0 OID 16449)
-- Dependencies: 219
-- Data for Name: componentviscosityimprovement; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3360 (class 0 OID 16403)
-- Dependencies: 212
-- Data for Name: mixcontainer; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mixcontainer (id, id_barcode, id_process, viscosity, t_start, t_end, t_end_tare, t_start_container, t_end_container, t_start_viscosity, t_end_viscosity) VALUES (1, 10025, 1, 9, '2022-06-27 09:35:20', '2022-06-27 09:55:20', '2022-06-27 09:48:20', '2022-06-27 09:49:50', '2022-06-27 09:53:00', '2022-06-27 09:53:20', '2022-06-27 09:55:00');


--
-- TOC entry 3358 (class 0 OID 16396)
-- Dependencies: 210
-- Data for Name: mixingprocess; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (1, 1, 'Arturo García', 3, 2, 3, '2022-06-27 09:30:20', '2022-06-27 10:30:20', 8, 10);
INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (2, 1, 'Arturo García', 4, 1, 2, '2022-06-27 11:20:00', '2022-06-27 12:20:00', 6, 9);
INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (3, 2, 'Franco', 1, 3, 5, '2022-06-27 10:25:00', '2022-06-27 11:15:00', 5, 7);
INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (5, 2, 'Franco', 2, 3, 1, '2022-06-27 18:55:51.992', '2022-06-27 20:55:51.992', 7, 8);
INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (6, 2, 'Franco', 2, 3, 1, '2022-06-27 18:57:42.103', '2022-06-27 20:57:42.103', 7, 8);
INSERT INTO public.mixingprocess (id, id_worker, name_worker, id_formula, id_filter, num_containers, t_start, t_end, expected_viscosity_min, expected_viscosity_max) VALUES (7, 3, 'José', 1, 2, 3, '2022-06-27 19:34:12.098', '2022-06-27 20:34:12.098', 6, 9);


--
-- TOC entry 3363 (class 0 OID 16426)
-- Dependencies: 215
-- Data for Name: processcontainercomponent; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3362 (class 0 OID 16415)
-- Dependencies: 214
-- Data for Name: viscosityimprovement; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 3382 (class 0 OID 0)
-- Dependencies: 220
-- Name: MixContainer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."MixContainer_id_seq"', 1, false);


--
-- TOC entry 3383 (class 0 OID 0)
-- Dependencies: 216
-- Name: componenttare_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.componenttare_id_seq', 1, false);


--
-- TOC entry 3384 (class 0 OID 0)
-- Dependencies: 218
-- Name: componentviscosityimprovement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.componentviscosityimprovement_id_seq', 1, false);


--
-- TOC entry 3385 (class 0 OID 0)
-- Dependencies: 211
-- Name: mixcontainer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mixcontainer_id_seq', 1, true);


--
-- TOC entry 3386 (class 0 OID 0)
-- Dependencies: 209
-- Name: mixingprocess_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mixingprocess_id_seq', 7, true);


--
-- TOC entry 3387 (class 0 OID 0)
-- Dependencies: 213
-- Name: viscosityimprovement_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.viscosityimprovement_id_seq', 1, false);


--
-- TOC entry 3212 (class 2606 OID 16466)
-- Name: MixContainer MixContainer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."MixContainer"
    ADD CONSTRAINT "MixContainer_pkey" PRIMARY KEY (id);


--
-- TOC entry 3208 (class 2606 OID 16442)
-- Name: componenttare componenttare_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componenttare
    ADD CONSTRAINT componenttare_pkey PRIMARY KEY (id);


--
-- TOC entry 3210 (class 2606 OID 16454)
-- Name: componentviscosityimprovement componentviscosityimprovement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componentviscosityimprovement
    ADD CONSTRAINT componentviscosityimprovement_pkey PRIMARY KEY (id);


--
-- TOC entry 3202 (class 2606 OID 16408)
-- Name: mixcontainer mixcontainer_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mixcontainer
    ADD CONSTRAINT mixcontainer_pkey PRIMARY KEY (id);


--
-- TOC entry 3200 (class 2606 OID 16401)
-- Name: mixingprocess mixingprocess_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mixingprocess
    ADD CONSTRAINT mixingprocess_pkey PRIMARY KEY (id);


--
-- TOC entry 3206 (class 2606 OID 16430)
-- Name: processcontainercomponent processcontainercomponent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.processcontainercomponent
    ADD CONSTRAINT processcontainercomponent_pkey PRIMARY KEY (id_mix_container, id_component);


--
-- TOC entry 3204 (class 2606 OID 16420)
-- Name: viscosityimprovement viscosityimprovement_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viscosityimprovement
    ADD CONSTRAINT viscosityimprovement_pkey PRIMARY KEY (id);


--
-- TOC entry 3216 (class 2606 OID 16443)
-- Name: componenttare componenttare_id_mix_container_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componenttare
    ADD CONSTRAINT componenttare_id_mix_container_fkey FOREIGN KEY (id_mix_container) REFERENCES public.mixcontainer(id);


--
-- TOC entry 3217 (class 2606 OID 16455)
-- Name: componentviscosityimprovement componentviscosityimprovement_id_viscosity_improvement_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.componentviscosityimprovement
    ADD CONSTRAINT componentviscosityimprovement_id_viscosity_improvement_fkey FOREIGN KEY (id_viscosity_improvement) REFERENCES public.viscosityimprovement(id);


--
-- TOC entry 3213 (class 2606 OID 16409)
-- Name: mixcontainer mixcontainer_id_process_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mixcontainer
    ADD CONSTRAINT mixcontainer_id_process_fkey FOREIGN KEY (id_process) REFERENCES public.mixingprocess(id);


--
-- TOC entry 3215 (class 2606 OID 16431)
-- Name: processcontainercomponent processcontainercomponent_id_mix_container_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.processcontainercomponent
    ADD CONSTRAINT processcontainercomponent_id_mix_container_fkey FOREIGN KEY (id_mix_container) REFERENCES public.mixcontainer(id);


--
-- TOC entry 3214 (class 2606 OID 16421)
-- Name: viscosityimprovement viscosityimprovement_id_mix_container_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.viscosityimprovement
    ADD CONSTRAINT viscosityimprovement_id_mix_container_fkey FOREIGN KEY (id_mix_container) REFERENCES public.mixcontainer(id);


-- Completed on 2022-06-27 20:22:49

--
-- PostgreSQL database dump complete
--

