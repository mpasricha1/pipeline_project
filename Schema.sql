DROP TABLE IF EXISTS pipelines;
DROP TABLE IF EXISTS pipeline_locations; 
DROP TABLE IF EXISTS flow_readings;

CREATE TABLE pipelines
(
    id integer NOT NULL,
    name character varying ,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    provider character varying ,
    code character varying ,
    tsp integer,
    loc_file_url character varying,
    flow_file_url character varying,
    CONSTRAINT pipelines_pkey PRIMARY KEY (id)
);

CREATE TABLE public.pipeline_location
(
    id integer NOT NULL,
    pipeline_id integer,
    loc_id character varying,
    name character varying,
    state character varying,
    county character varying,
    zone character varying,
    loc_type character varying,
    flow_direction character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    has_missing_details boolean,
    CONSTRAINT pipeline_location_pkey PRIMARY KEY (id),
    CONSTRAINT pipeline_location_pipeline_id_fkey FOREIGN KEY (pipeline_id)
        REFERENCES public.pipelines (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE public.flow_readings
(
    id integer NOT NULL,
    pipeline_location_id integer,
    loc_id character varying,
    flow_date date,
    tsq integer,
    flow_dir character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    cycle_desc character varying,
    oc integer,
    CONSTRAINT flow_readings_pkey PRIMARY KEY (id),
    CONSTRAINT flow_readings_pipeline_location_id_fkey FOREIGN KEY (pipeline_location_id)
        REFERENCES public.pipeline_location (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);