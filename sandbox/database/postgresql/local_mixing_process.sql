-- PostgressSQL .. 

--  local_mixing_process; 
-- /*
DROP TABLE IF EXISTS ProcessContainerComponent;
DROP TABLE IF EXISTS ComponentTare;
DROP TABLE IF EXISTS ComponentViscosityImprovement;
DROP TABLE IF EXISTS ViscosityImprovement;
DROP TABLE IF EXISTS MixContainer;
DROP TABLE IF EXISTS MixingProcess;
DROP TABLE IF EXISTS MachineInformation;

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
    name_worker varchar(64),
    id_formula int NOT NULL,
    id_filter int NOT NULL,
    num_containers int NOT NULL,
    conatiner_base_weight float NOT NULL, -- the weight used to calculate the weights for each component; for now is 8000g
    t_start timestamp,
    t_end timestamp,
    expected_viscosity_min float NOT NULL,
    expected_viscosity_max float NOT NULL,
    PRIMARY KEY (id)
);


CREATE TABLE MixContainer(
	id serial NOT NULL, 
    id_barcode int NOT NULL, -- keeps the barcode id of the container
    id_process integer NOT NULL, -- from MixingProcess
    viscosity float,
    weight float,
    humidity float, -- porcentaje de humedad ... 
    temperature float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    t_start_tare timestamp, -- for all the tares .. 
    t_end_tare timestamp,-- for all the tares ..
    t_start_container timestamp,
    t_end_container timestamp,
    t_start_viscosity timestamp,
    t_end_viscosity timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_process) REFERENCES MixingProcess(id)
);

CREATE TABLE ViscosityImprovement(
	id serial NOT NULL, 
    id_mix_container integer NOT NULL, -- from MixingContainer
    new_viscosity float,
    extra_weight float, -- new added weight 
    t_start timestamp NOT NULL,
    t_end timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
);

-- keeps the total weight for each process-container
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
    PRIMARY KEY (id),
    FOREIGN KEY (id_mix_container) REFERENCES MixContainer(id)
);


CREATE TABLE ComponentViscosityImprovement(
	id serial NOT NULL,
    id_viscosity_improvement integer NOT NULL, -- from ViscosityImprovement
    id_component int NOT NULL, -- from json Component file .. 
    extra_weight float,
    t_start timestamp NOT NULL,
    t_end timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (id_viscosity_improvement) REFERENCES ViscosityImprovement(id)
);

INSERT INTO public.machineinformation (id_in, name, description, start_up) VALUES ('XFc340PG', 'Maquina No. 1 de Prcoeso de Mezclado', 'Máquina para registrar y trazar el proceso de mezclado de pintura para los diferentes modelos', '2022-07-03 12:00:00');
-- */
