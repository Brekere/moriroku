-- QUERYS to pass JSON to DB records
-- Querys Suppliers
INSERT INTO suppliers (name, description, rfc, address, tel) VALUES (“Mankiewicz”)

-- Querys ComponentsQRInfo
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '9016J.0000.0.006', 0025, 5, 0, 2023, 02);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '901B9.0000.0.006', 0029, 5, 0, 2022, 09);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '40596.0000.0.002', 0069, 6, 0, 2022, 09);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '9001B9.0000.0.006', 0024, 5, 0, 2022, 02);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4611M.53LN.1.556', 0020, 15, 0, 2023, 10);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.9MJM.7.556', 0009, 15, 0, 2023, 02);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '40596.0000.0.002', 0071, 6, 0, 2022, 11);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.2958.7.556', 0006, 15, 0, 2023, 02);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '40550.0000.0.559', 1403, 20, 0, 2022, 05);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4611M.59CB.1.011', 0011, 25, 0, 2023, 11);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4611M.53LN.1.556', 0019, 15, 0, 2023, 09);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '40550.0000.0.559', 1436, 20, 0, 2022, 08);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.99V7.1.556', 0014, 15, 0, 2023, 02);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4601G.0000.9.011', 0028, 25, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.9MJM.7.556', 0008, 15, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '90186.0000.0.556', 1097, 15, 0, 2024, 05);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '90389.0000.0.556', 0135, 15, 0, 2023, 08);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.9MFS.1.556', 0012, 15, 0, 2023, 03);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, expiration_year, expiration_month) VALUES (1, 'LN245.0009.6.000', 0001, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '4613P.2958.7.556', 0005, 15, 0, 2023, 01);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '90019.0000.0.004', 0005, 1, 3, 2020, 06);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '460SR.90ZC.M.011', 0029, 25, 0, 2022, 10);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '460SR.90ZC.M.011', 0028, 25, 0, 2022, 10);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '460SR.90ZC.M.011', 0040, 25, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '460SR.90ZC.M.011', 0041, 25, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '460SR.90ZC.M.011', 0043, 25, 0, 2022, 12);
INSERT INTO componentsqrinfo (id_supplier, identifier, batch, weight, weight_type, expiration_year, expiration_month) VALUES (1, '90019.0000.0.004', 0005, 1, 3, 2020, 06);

-- Querys ComponentType
INSERT INTO componenttype (name) VALUES ('Base');
INSERT INTO componenttype (name) VALUES ('Solvente');
INSERT INTO componenttype (name) VALUES ('Aditivo');
INSERT INTO componenttype (name) VALUES ('Catalizador');

-- Querys Components
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (2, '901B9', '901-B9', '901B9.0000.0.006', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (2, '90186', '901-86', '90186.0000.0.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (2, '90019', '909-1N', '90019.0000.0004', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (2, '90389', '903-89', '90389.0000.0.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '460SR', 'Piano Black', '460SR.90ZC.M.011', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4613P', 'Caribou Gray', '4613P.9MFS.1.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4611M', 'Dark Blue', '4611M.53LN.1.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4613P', 'Deep Iron', '4613P.99V7.1.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4611M', 'Dark Marine', '4611M.59CB.1.011', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4613P', 'Cappuccino Beige', '4613P.9MJM.7.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4613P', 'Energetic Orange', '4613P.2958.7.556', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (1, '4601G', 'Clear Coat', '4601G.0000.9.011', true);
INSERT INTO components (id_type, name, nick_name, identifier, in_use) VALUES (3, 'LN245', '100611', 'LN245.0009.6.000', true);

-- Querys Models
INSERT INTO models (part_number) VALUES ('2GJ.858.415.001');
INSERT INTO models (part_number) VALUES ('2GJ.858.415.002');
INSERT INTO models (part_number) VALUES ('2GJ.858.415.003');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.001');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.A.002');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.B.003');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.C.004');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.D.005');
INSERT INTO models (part_number) VALUES ('2GJ.867.061.7N5');
INSERT INTO models (part_number) VALUES ('2GJ.867.061.8Z6');
INSERT INTO models (part_number) VALUES ('2GJ.867.061.3LB');
INSERT INTO models (part_number) VALUES ('2GJ.867.062.8Z6');
INSERT INTO models (part_number) VALUES ('2GJ.867.062.7N5');
INSERT INTO models (part_number) VALUES ('2GJ.867.062.A.8Z6');
INSERT INTO models (part_number) VALUES ('2GJ.867.062.A.3LB');
INSERT INTO models (part_number) VALUES ('2GJ.867.439.4.7N5');
INSERT INTO models (part_number) VALUES ('2GJ.867.440.A.7N5');
INSERT INTO models (part_number) VALUES ('2GJ.867.440.C.7N5');
INSERT INTO models (part_number) VALUES ('2GJ.867.439.A.7P7');
INSERT INTO models (part_number) VALUES ('2GJ.867.440.C.7P7');
INSERT INTO models (part_number) VALUES ('2GJ.867.439.A.9D9');
INSERT INTO models (part_number) VALUES ('2GJ.867.440.C.9D9');
INSERT INTO models (part_number) VALUES ('2GJ.867.061.3LC');
INSERT INTO models (part_number) VALUES ('2GJ.867.062A.3LC');
INSERT INTO models (part_number) VALUES ('2GJ.867.061.9D9');
INSERT INTO models (part_number) VALUES ('2GJ.867.062A.9D9');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.D.004');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.C.001');
INSERT INTO models (part_number) VALUES ('2GJ.858.415.E');
INSERT INTO models (part_number) VALUES ('2GJ.858.415.003.J');
INSERT INTO models (part_number) VALUES ('2GJ.858.416.F.005');

-- Querys ColorsFormulas
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('041', 'Piano Black', 5.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('8Z6', 'Caribou Gray', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('7N5', 'Dark Blue', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('3LB', 'Deep Iron', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('7P7', 'Dark Marine', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('9D9', 'Cappuccino Beige', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('3LC', 'Energetic Orange', 6.0, 8.0);
INSERT INTO colorsformulas (color_code, name, min_viscosity, max_viscosity) values ('0L9', 'Clear Coat', 5.0, 10.0);

-- Querys ColorsModels
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400001, 1, 1, 'VISOR PINTADO FS TL PIANO BLACK', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400002, 3, 2, 'VISOR PINTADO FS CL DARK BLUE', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400003, 5, 2, 'VISOR PINTADO FS CL DARK MARINE', 24.975);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400004, 6, 2, 'VISOR PINTADO FS CL CAPUCCINO BEIGE', 35.9964);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400005, 2, 3, 'VISOR PINTADO FS HL & CL CARIBOU GRAY', 31.550178);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400006, 4, 3, 'VISOR PINTADO FS HL & CL DEEP IRON', 33.33);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400007, 7, 3, 'VISOR PINTADO FS HL & CL ENERGETIC ORANGE', 35.9964);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400008, 1, 3, 'VISOR PINTADO FS HL & CL PIANO BLACK', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400009, 3, 3, 'VISOR FS HL & CL PINTADO DARK BLUE', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400011, 1, 4, 'VISOR PINTADO BFS 6.5 TL PIANO BLACK', 58.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400012, 3, 5, 'VISOR PINTADO BFS CL 8.0 DARK BLUE', 36.21375);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400013, 3, 6, 'VISOR PINTADO BFS HL 8.0 DARK BLUE', 36.21375);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400014, 2, 6, 'VISOR PINTADO BFS CL 8.0 CARIBOU GRAY', 53.328);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400015, 5, 7, 'VISOR PINTADO BFS CL 10.0 DARK MARINE', 37.4625);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400016, 6, 7, 'VISOR PINTADO BFS CL 10.0 CAPUCCINO BEIGE', 51.3282);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400017, 3, 7, 'VISOR PINTADO BFS CL 10.0 DARK BLUE', 36.21375);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400018, 4, 8, 'VISOR PINTADO BFS HL 10.0 DEEP IRON', 51.3282);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400019, 7, 8, 'VISOR PINTADO BFS HL 10.0 ENERGETIC ORANGE', 59.994);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400020, 2, 8, 'VISOR PINTADO BFS HL 10.0 CARIBOU GRAY', 53.328);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400021, 1, 8, 'VISOR PINTADO BFS HL 10.0 PIANO BLACK', 58.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400022, 3, 9, 'PUERTA TIB CL IZQ CON/SW DARK BLUE', 11.1);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400023, 2, 10, 'PUERTA TIB HL IZQ CON/SW CARIBOU GRAY', 17.9982);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400024, 4, 11, 'PUERTA TIB HL IZQ CON/SW DEEP IRON', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400025, 2, 12, 'PUERTA TIB HL DER CON/SW CARIBOU GRAY', 17.9982);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400026, 3, 13, 'PUERTA TIB HL DER CON/SW DARK BLUE', 11.1);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400027, 2, 14, 'PUERTA TIB HL DER SIN/SW CARIBOU GRAY', 17.9982);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400028, 4, 15, 'PUERTA TIB HL DER SIN/SW DEEP IRON', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400029, 3, 16, 'PUERTA TIB CL IZQ CON/SW DARK BLUE', 11.1);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400030, 3, 17, 'PUERTA TIB CL DER CON/SW DARK BLUE', 11.1);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400031, 3, 18, 'PUERTA TIB CL DER SIN/SW DARK BLUE', 11.1);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400032, 5, 19, 'PUERTA TIB CL IZQ CON/SW DARK MARINE', 12.765);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400033, 5, 20, 'PUERTA TIB CL DER SIN/SW DARK MARINE', 12.765);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400034, 6, 21, 'PUERTA TIB CL IZQ CON/SW CAPUCCINO BEIGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400035, 6, 22, 'PUERTA TIB CL DER SIN/SW CAPUCCINO BEIGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400036, 7, 23, 'PUERTA TIB HL IZQ CON/SW ENERGETIC ORANGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400037, 7, 24, 'PUERTA TIB HL DER CON/SW ENERGETIC ORANGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400038, 6, 25, 'PUERTA TIB HL IZQ CON/SW CAPUCCINO BEIGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400039, 6, 26, 'PUERTA TIB HL DER SIN/SW CAPUCCINO BEIGE', 19.998);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400040, 6, 2, 'VISOR PINTADO FS CL/HL CAPUCCINO BEIGE', 35.9964);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400041, 6, 27, 'VISOR PINTADO BFS HL 10.0 CAPUCCINO BEIGE', 51.3282);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400042, 1, 28, 'VISOR PINTADO BFS 6.5 TL PIANO BLACK', 58.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400043, 1, 29, 'VISOR PINTADO FS TL PIANO BLACK 10\', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400044, 1, 30, 'VISOR PINTADO FS F/G PIANO BLACK', 23.331);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400045, 1, 31, 'VISOR PINTADO BFS HL 10.0 PIANO BLACK', 58.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400049, 8, 2, 'VISOR PINTADO FS CL CAPUCCIONO BEIGE', 25.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400050, 8, 3, 'VISOR PINTADO FS HL & CL CARIBOU GRAY', 19.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400051, 8, 3, 'VISOR PINTADO FS HL & CL DEEP IRON', 21.83);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400052, 8, 3, 'VISOR PINTADO FS HL & CL ENERGETIC ORANGE', 29.75);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400059, 8, 6, 'VISOR PINTADO BFS CL 8.0 CARIBOU GRAY', 43.9956);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400061, 8, 7, 'VISOR PINTADO BFS CL 10.0 CAPUCCINO BEIGE', 43.9956);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400063, 8, 8, 'VISOR PINTADO BFS HL 10.0 DEEP IRON', 42.662400000000005);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400064, 8, 8, 'VISOR PINTADO BFS HL 10.0 ENERGETIC ORANGE', 44.16225);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400065, 8, 8, 'VISOR PINTADO BFS HL 10.0 CARIBOU GRAY', 43.9956);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400068, 8, 10, 'PUERTA TIB HL IZQ CON/SW CARIBOU GRAY', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400069, 8, 11, 'PUERTA TIB HL IZQ CON/SW DEEP IRON', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400070, 8, 12, 'PUERTA TIB HL DER CON/SW CARIBOU GRAY', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400072, 8, 14, 'PUERTA TIB HL DER SIN/SW CARIBOU GRAY', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400073, 8, 15, 'PUERTA TIB DER SIN/SW DEEP IRON', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400079, 8, 21, 'PUERTA TIB CL IZQ CON/SW CAPUCCINO BEIGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400080, 8, 22, 'PUERTA TIB CL DER SIN/SW CAPUCCINO BEIGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400081, 8, 23, 'PUERTA TIB HL IZQ CON/SW ENERGETIC ORANGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400082, 8, 24, 'PUERTA TIB HL DER CON/SW ENERGETIC ORANGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400083, 8, 25, 'PUERTA TIB HL IZQ CON/SW CAPUCCINO BEIGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400084, 8, 26, 'PUERTA TIB HL DER SIN/SW CAPUCCINO BEIGE', 9.25);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400085, 8, 2, 'VISOR PINTADO FS CL/HL CAPUCCINO BEIGE', 25.0);
INSERT INTO colorsmodels (id_, id_color, id_model, description, base_weight) values (102400086, 8, 27, 'VISOR PINTADO BFS HL 10.0 CAPUCCINO BEIGE', 43.9956);

-- Querys ContainersInfo
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('123423', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('234112', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('131307', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('001204', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('000001', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('187932', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('202207', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('220713', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('150722', current_date, 18, 0);
INSERT INTO containersinfo (id_barcode, date_creation, weight_kg, container_type) values ('130513', current_date, 18, 0);

-- Querys Filters
INSERT INTO filters (size_micron, name) VALUES (25, 'Filtro de 25 micras');
INSERT INTO filters (size_micron, name) VALUES (50, 'Filtro de 50 micras');
INSERT INTO filters (size_micron, name) VALUES (75, 'Filtro de 75 micras');
INSERT INTO filters (size_micron, name) VALUES (100, 'Filtro de 100 micras');

-- Querys FiltersColors
INSERT INTO filterscolors (id_color, id_filter) values (1, 1);
INSERT INTO filterscolors (id_color, id_filter) values (2, 2);
INSERT INTO filterscolors (id_color, id_filter) values (3, 3);
INSERT INTO filterscolors (id_color, id_filter) values (4, 3);
INSERT INTO filterscolors (id_color, id_filter) values (5, 4);
INSERT INTO filterscolors (id_color, id_filter) values (6, 4);
INSERT INTO filterscolors (id_color, id_filter) values (7, 3);
INSERT INTO filterscolors (id_color, id_filter) values (8, 2);

	-- Querys FormulasComponents
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (1, 5, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (1, 1, 20.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (1, 2, 20.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (1, 3, 5.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (1, 13, 1.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (2, 6, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (2, 2, 35.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (2, 4, 15.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (3, 7, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (3, 2, 80.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (4, 8, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (4, 4, 50.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (5, 9, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (5, 2, 80.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (6, 10, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (6, 4, 50.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (7, 11, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (7, 4, 50.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (8, 12, 100.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (8, 4, 50.0, 1.0);
INSERT INTO formulascomponents (id_color_formula, id_component, percentage, tolerance) values (8, 13, 1.0, 1.0);

-- Querys Job Positions
INSERT INTO jobspositions (name) VALUES ('Assistant Manager');
INSERT INTO jobspositions (name) VALUES ('Group Leader');
INSERT INTO jobspositions (name) VALUES ('Team Leader');
INSERT INTO jobspositions (name) VALUES ('Jr. Team Leader');

-- Querys Workers
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (121, 'Heber Ramírez Carrera', 1);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (147, 'José Carlos Vargas Cruz', 3);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (191, 'Roberto Alomar Dominguez Calderon', 2);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (129, 'Javier Aguirre Rangel', 4);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (125, 'Ricardo Rey Rocha', 3);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (138, 'Francisco Ruiz Segundo', 2);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (472, 'Armando Sánchez Suarez', 2);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (47, 'Elena de la soledad Almaguer Benitez', 3);
INSERT INTO usersworkers (payroll_number, name, id_job_position) VALUES (24, 'Anahí Celaya', 3);

--Querys ImprovedWix
--PIANO BLACK
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (1, 2, 2, 1.0, 100, true);
--Caribou Gray
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (2, 2, 4, 1.0, 100, true);
--Dark Blue
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (3, 2, 2, 1.0, 100, true);
--Deep Iron
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (4, 2, 4, 1.0, 100, true);
--Dark Marine
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (5, 2, 2, 1.0, 100, true);
--Capuccino Beige
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (6, 2, 2, 1.0, 100, true);
--Energetic Orange
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (7, 2, 2, 1.0, 100, true);
--Clear Coat
INSERT INTO improvedmix (id_formula, id_type_component, id_component, tolerance, weight_g, in_use) values (8, 2, 2, 1.0, 100, true);
