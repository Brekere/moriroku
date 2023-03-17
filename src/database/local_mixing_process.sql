-- PostgressSQL .. 

--  local_mixing_process; 
-- /*
DROP TABLE IF EXISTS ProcessContainerComponent;
DROP TABLE IF EXISTS ProcessStepReleasesInfo;
DROP TABLE IF EXISTS ProcessReleasesTypes;
DROP TABLE IF EXISTS ComponentTare;
DROP TABLE IF EXISTS ComponentViscosityImprovement;
--DROP TABLE IF EXISTS ViscosityImprovement;
DROP TABLE IF EXISTS MixContainer;
DROP TABLE IF EXISTS MixingProcessStatus;
DROP TABLE IF EXISTS ZPLCodeMixingProcess; -- new
DROP TABLE IF EXISTS MixingProcess;
DROP TABLE IF EXISTS MachineMixingProcess; -- new
DROP TABLE IF EXISTS MachineInformation;

DROP TABLE IF EXISTS FormulasComponents;
DROP TABLE IF EXISTS FiltersColors;
DROP TABLE IF EXISTS Filters;
DROP TABLE IF EXISTS ContainersInfo;
DROP TABLE IF EXISTS ColorsModels;
DROP TABLE IF EXISTS ColorsFormulas;
DROP TABLE IF EXISTS Models;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Components;
DROP TABLE IF EXISTS ComponentType;
DROP TABLE IF EXISTS ComponentsQRInfo;
DROP TABLE IF EXISTS Suppliers;
DROP TABLE IF EXISTS JobsPositions;
DROP TABLE IF EXISTS UsersWorkers;

--- Creando Tablas .. 
CREATE TABLE MachineInformation (
	id serial NOT NULL,
    id_in varchar(16) NOT NULL, -- id_ given by the company
    name varchar(64) NOT NULL,
    description varchar(512) NOT NULL,
    start_up timestamp NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id_in)
);

CREATE TABLE MixingProcess (
	id serial NOT NULL,
    id_worker int NOT NULL,
    name_worker varchar(64) not NULL,
    id_formula int NOT NULL,
    id_filter int NOT NULL,
    num_containers int NOT NULL,
    conatiner_base_weight float NOT NULL, -- the weight used to calculate the weights for each component; for now is 8000g
    t_start timestamp,
    t_end timestamp,
    expected_viscosity_min float NOT NULL,
    expected_viscosity_max float NOT NULL,
    number_of_pieces int not NULL,
    grams_to_recirculate int not NULL,
    work_order varchar(16) not NULL,
    id_model int not NULL,
    -- Para darle seguimiento cuando el proceso se detiene por la temperatura, o por cualquier otro motivo ... 
    failed_process boolean, --- si el proceso falla, principalmente por temperatura
    failure_type  int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)
    failure_description varchar(1024), -- una pequeña descripción dada por el sistema de por que el fallo (esto aún no se pondra en funcionalidad) 
    PRIMARY KEY (id)
);

-- Table that keeps the ZPL code for a Mixing Process (Nueva)
CREATE TABLE ZPLCodeMixingProcess(
    id int not NULL,
    zpl_code TEXT, -- ver como se usa en python (con PostgreSQL y con SQL Server)
    creation_date timestamp,
    update_date timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES MixingProcess(id)
)

-- Relationship between Machine and Mixing Process (Nueva)
CREATE TABLE MachineMixingProcess(
    --id serial NOT NULl,
    id_process int NOT NULL,
    id_machine int not NULL,
    --PRIMARY KEY (id),
    PRIMARY KEY (id_process, id_machine),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id),
    FOREIGN KEY (id_machine) REFERENCES MachineInformation(id)
)

-- to kept track when crahsed the system
CREATE TABLE MixingProcessStatus (
	id serial NOT NULL,
    id_process int NOT NULL,
    t_event_registration timestamp NOT NULL,
    status int NOT NULL, -- 0 -> started, 1 -> some containers where registered, 3 -> all containers registered, 4 -> viscosity imrpovement in process, 5 -> all process is ok
    notes varchar(1024), -- some short notes 
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
);

CREATE TABLE MixContainer(
	id serial NOT NULL, 
    id_barcode int, -- keeps the barcode id of the container; it is updated until the final component (base)
    id_process integer NOT NULL, -- from MixingProcess
    viscosity float,
    weight float,
    humidity float, -- porcentaje de humedad ... 
    temperature float,
    t_start timestamp NOT NULL, -- the whole process
    t_end timestamp,
    t_start_tare timestamp, -- for all the tares .. 
    t_end_tare timestamp,-- for all the tares ..
    t_start_container timestamp,
    t_end_container timestamp,
    t_start_viscosity timestamp,
    t_end_viscosity timestamp,
    failed_process boolean, --- si el proceso falla, principalmente por temperatura
    failure_type  int, --- tipo de falla ... 0 -> temperatura, 1 -> otros (solo hay un caso definido por ahora)
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
);

-- CREATE TABLE ViscosityImprovement(
--	id serial NOT NULL, 
--    id_mix_container integer NOT NULL, -- from MixingContainer
--    new_viscosity float,
--    extra_weight float, -- new added weight 
--    t_start timestamp NOT NULL,
--    t_end timestamp,
--    PRIMARY KEY (id),
--    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
--);

-- keeps the total weight for each process-container (maybe it will not needed)
CREATE TABLE ProcessContainerComponent(
	id_mix_container integer NOT NULL, -- from MixingContainer
    id_type_component int NOT NULL, -- from json file where are types and component type name ..
    id_component int NOT NULL, -- from json Component file .. 
    weight float NOT NULL,
    PRIMARY KEY (id_mix_container, id_component),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
);

--  ###### Llevar registros más exactos ... 
CREATE TABLE ComponentTare(
	id serial NOT NULL,
    id_mix_container integer NOT NULL, -- from MixingContainer
    id_type_compoennt int NOT NULL, -- from json 
    id_component int NOT NULL, -- from json Component file .. 
    weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    batch varchar(8),-- save the lote number of the component ... 
    batch_expiration DATE NOT NULL, --- just need year and month
    PRIMARY KEY (id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
);


CREATE TABLE ComponentViscosityImprovement(
	id serial NOT NULL,
    --id_viscosity_improvement integer NOT NULL, -- from ViscosityImprovement
    id_component int NOT NULL, -- from json Component file .. 
    id_mix_container integer NOT NULL, -- from MixingContainer
    new_viscosity float,
    extra_weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    batch varchar(8),-- save the lote number of the component ...
    PRIMARY KEY (id),
    --FOREIGN KEY (id_viscosity_improvement) REFERENCES ViscosityImprovement(id)
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
);

--- Table that keeps the information of the liberations

CREATE TABLE ProcessReleasesTypes(
    id serial NOT NULL, -- 0 expiration of a component, 1 special case for small witgh in a poor resolution scale (2gr)
    name varchar(64) NOT NULL,
    description varchar(512) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE ProcessStepReleasesInfo(
    id serial NOT NULL,
    id_process integer NOT NULL,
    id_worker integer NOT NULL, --- worker that made the release...
    id_type_release int NOT NULL, 
    time_stamp timestamp NOT NULL, --- fecha que hizo el evento 
    id_component_tare integer,
    id_container integer, 
    PRIMARY KEY (id),
    FOREIGN KEY (id_type_release) REFERENCES ProcessReleasesTypes(id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id),
    FOREIGN KEY (id_container) REFERENCES MixContainer(id),
    FOREIGN KEY (id_component_tare) REFERENCES ComponentTare(id)
);

------- json file Tables
--CREATE TABLE name(
--    PRIMARY KEY (id),
--    FOREIGN KEY (key) REFERENCES table(id),
--);

CREATE TABLE Suppliers(
    id serial NOT NULL,
    name varchar(64) NOT NULL, 
    description varchar(512),
    rfc varchar(14),
    address varchar(64),
    tel varchar(14),
    PRIMARY KEY (id)
);

CREATE TABLE ComponentsQRInfo(
    id serial NOT NULL,
    id_supplier integer NOT NULL,
    identifier varchar(20) NOT NULL,
    batch int NOT NULL,
    weight float NOT NULL,
    weight_type int NOT NULL, -- 0 kg, 1 g, 2 lb
    expiration_year int NOT NULL,
    expiration_month int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_supplier) REFERENCES Suppliers(id)
);

CREATE TABLE ComponentType(
    id serial NOT NULL,
    name varchar(20) NOT NULL,
    description varchar(512),
    PRIMARY KEY (id)
);


CREATE TABLE Components(
    id serial NOT NULL,
    id_type integer NOT NULL,
    name varchar(20) NOT NULL,
    nick_name varchar(20) NOT NULL,
    identifier varchar(20) NOT NULL, -- used to check in QR's info
    description varchar(256),
    in_use bool NOT NULL,
    -- id_qr_info integer NOT NULL,
    PRIMARY KEY (id),
    -- FOREIGN KEY (id_qr_info) REFERENCES ComponentsQRInfo(id),
    FOREIGN KEY (id_type) REFERENCES ComponentType(id)
);

CREATE TABLE Clients(
    id serial NOT NULL,
    name varchar(32) NOT NULL,
    description varchar(256),
    PRIMARY KEY (id)
);

CREATE TABLE Models(
    id serial NOT NULL,
    id_client integer NOT NULL,
    part_number varchar(16) NOT NULL,
    description varchar(256),
    PRIMARY KEY (id),
    FOREIGN KEY (id_client) REFERENCES Clients(id)
);

CREATE TABLE ColorsFormulas(
    id serial NOT NULL,
    color_code varchar(4) NOT NULL,
    name varchar(32) NOT NULL,
    min_viscosity float NOT NULL,
    max_viscosity float NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE ColorsModels(
    id serial NOT NULL,  -- internal id
    id_ integer NOT NULL, -- given by Moriroku "pintado"
    id_color integer NOT NULL,
    id_model integer NOT NULL,
    description varchar(128), -- same as PaintedWeight.description
    base_weight float NOT NULL, -- in grams
    PRIMARY KEY (id),
    FOREIGN KEY (id_color) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_model) REFERENCES Models(id)
);
/*
-- Not needed .. the relevant information is in the previous table  
CREATE TABLE PaintedWeight(
    id serial NOT NULL, -- pintado
    description varchar(128),
    id_color_formula integer NOT NULL,
    id_model integer NOT NULL,
    base_weight float NOT NULL, -- in grams
    PRIMARY KEY (id),
    FOREIGN KEY (id_color_formula) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_model) REFERENCES Models(id),
);
*/

CREATE TABLE ContainersInfo(
    id serial NOT NULL,
    id_barcode varchar(8) NOT NULL,
    date_creation timestamp NOT NULL,
    weight_kg float NOT NULL,
    container_type int NOT NULL, -- 0 metal, 1 thin plastic, 2 thick plastic
    PRIMARY KEY (id)
);

CREATE TABLE Filters(
    id serial NOT NULL,
    size_micron float NOT NULL,
    name varchar(32) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE FiltersColors(
    id_color integer NOT NULL,
    id_filter integer NOT NULL,
    PRIMARY KEY (id_color,id_filter),
    FOREIGN KEY (id_color) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_filter) REFERENCES Filters(id)
);


CREATE TABLE FormulasComponents(
    id_color_formula integer NOT NULL,
    id_component integer NOT NULL,
    percentage float NOT NULL,
    tolerance float NOT NULL,
    PRIMARY KEY (id_color_formula, id_component),
    FOREIGN KEY (id_color_formula) REFERENCES ColorsFormulas(id),
    FOREIGN KEY (id_component) REFERENCES Components(id)
);


CREATE TABLE JobsPositions(
    id serial NOT NULL,
    name varchar(32) NOT NULL,
    description varchar(256),
    PRIMARY KEY (id)
);

CREATE TABLE UsersWorkers(
    id serial NOT NULL,
    payroll_number integer NOT NULL,
    name varchar(80) NOT NULL,
    id_job_position integer NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_job_position) REFERENCES JobPosition(id)
);

--- Creating basic records ... 

INSERT INTO public.machineinformation (id_in, name, description, start_up) VALUES ('M1', 'Maquina No. 1 de Prcoeso de Mezclado', 'Máquina para registrar y trazar el proceso de mezclado de pintura para los diferentes modelos', '2022-07-13 12:00:00');


INSERT INTO public.processreleasestypes(name, description) VALUES ('COMPONENT EXPIRATION DATE', 'Cuando valida el usuario que se use el componente aunque este caducado');
INSERT INTO public.processreleasestypes(name, description) VALUES ('SMALL WEIGHT RESOLUTION', 'Cuando la bascula tiene una resolución muy grande y no puede llegar a los limites esperados (nuestro caso 2gr de resolucion)');

-- */
