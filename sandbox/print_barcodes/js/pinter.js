var selected_device;
var devices = [];
function setup()
{
	//Get the default device from the application as a first step. Discovery takes longer to complete.
	BrowserPrint.getDefaultDevice("printer", function(device)
			{
		
				//Add device to list of devices and to html select element
				selected_device = device;
				devices.push(device);
				var html_select = document.getElementById("selected_device");
				var option = document.createElement("option");
				option.text = device.name;
				html_select.add(option);
				
				//Discover any other devices available to the application
				BrowserPrint.getLocalDevices(function(device_list){
					for(var i = 0; i < device_list.length; i++)
					{
						//Add device to list of devices and to html select element
						var device = device_list[i];
						if(!selected_device || device.uid != selected_device.uid)
						{
							devices.push(device);
							var option = document.createElement("option");
							option.text = device.name;
							option.value = device.uid;
							html_select.add(option);
						}
					}
					
				}, function(){alert("Error getting local devices")},"printer");
				
			}, function(error){
				alert(error);
			})
}
function getConfig(){
	BrowserPrint.getApplicationConfiguration(function(config){
		alert(JSON.stringify(config))
	}, function(error){
		alert(JSON.stringify(new BrowserPrint.ApplicationConfiguration()));
	})
}
function writeToSelectedPrinter(dataToWrite)
{
    console.log(dataToWrite);
	selected_device.send(dataToWrite, undefined, errorCallback);
}
var readCallback = function(readData) {
	if(readData === undefined || readData === null || readData === "")
	{
		alert("No Response from Device");
	}
	else
	{
		alert(readData);
	}
	
}
var errorCallback = function(errorMessage){
	alert("Error: " + errorMessage);	
}
function readFromSelectedPrinter()
{

	selected_device.read(readCallback, errorCallback);
	
}
function getDeviceCallback(deviceList)
{
	alert("Devices: \n" + JSON.stringify(deviceList, null, 4))
}

function sendFile(fileUrl){
    url = window.location.href.substring(0, window.location.href.lastIndexOf("/"));
    url = url + "/" + fileUrl;
    selected_device.sendFile(url, undefined, errorCallback)
}
function onDeviceSelected(selected)
{
	for(var i = 0; i < devices.length; ++i){
		if(selected.value == devices[i].uid)
		{
			selected_device = devices[i];
			return;
		}
	}
}

////// ----------------------------------------- 

var code_zpl = "";

var code_zpl_data = "";
function create_data_example(){
    t_start = new Date();
    data = {
        company: "Moriroku Technology",
        client: "TESLA",
        n_lote: 12,
        t_start: t_start,
        name_worker: "Arturo Garcia",
        id_worker: 13,
        container: "1/3",
        weight: 1100,
		type_w: "g",
        id_container: "13DF67A", // a código de barra ... 
        color_code: "7ND",
		color_name: "Piano BLACK",
        model: "5GT",
        components: [
            {
                component_type: "Base",
                component: "Piano Black",
                weight: 8100,
                type_w: "g"
            },
            {
                component_type: "Aditive",
                component: "11610",
                weight: 200,
                type_w: "g"
            },
        ], 
    } 

	return data;
}

var format_start = "^XA^LL200^FO80,50^A0N36,36^FD";
var format_end = "^FS^XZ";
var field_origin = "^FO";
var field_data = "^FD";
var title_height = 60;
var font_title = "0";
var field_separator="^FS";
var cr_lf = "_0D_0";

function zpl_text(text_){
	return field_data+text_;
}

function zpl_text_with_field_separator_qr(text_){
	return field_data+"XXX"+text_+field_separator;
}

function zpl_text_with_field_separator(text_){
	return field_data+text_+field_separator;
}

function zpl_font_(font_, font_h){
    return "^CF"+font_+","+font_h+"\n";
}

function zpl_field_origin(x,y){
	return field_origin+x+","+y;
}

function zpl_FieldData(text,x,y){
    //return field_origin+x+","+y+zpl_text_with_field_separator(text)+"\n";
	return zpl_field_origin(x,y)+zpl_text_with_field_separator(text)+"\n";
}

function zpl_FieldData_font(text,x,y,font_, font_h){
    return zpl_font_(font_, font_h)+zpl_FieldData(text,x,y,);
}

function create_title(text_company, text_client,x,y){
    origin_w = x;
    origin_h = y;
	font_h = 60;
	title_ = zpl_FieldData_font(text_company, origin_w, origin_h, "0",font_h);
    //title_ = "^CF0,60\n"+field_origin+origin_w+","+origin_h+field_data+text_company+field_separator+"\n";
    title_ += zpl_FieldData("Client: "+ text_client,origin_w+30,origin_h+font_h, "0", 30);
    return title_;
}
/*
function create_title_2(text_,x,y){
	return zpl_FieldData(text,x,y);
}
*/

function zpl_line(x,y, l_w, l_h){
	return "^FO"+x+","+y+"^GB"+l_w+","+l_h+",3^FS";
}

function zpl_qr_from_list(list_texts,x,y){
	text_ = "";
	//console.log(list_texts);
	console.log(" x: " + x + "  y: "+ y);
	list_texts.forEach( function(text_el, i){
		if(i == 0){
			text_+=text_el;
		}else{
			text_+=";"+text_el;
		}
		//console.log(i+") " + text_);
	});
	text_ = "^FO"+x+","+y+"\n^BQ,2,6" + zpl_text_with_field_separator_qr(text_)
	return text_;
}

function zpl_qr_from_list_2(list_texts,x,y){
	text_ = "";
	//console.log(list_texts);
	console.log(" x: " + x + "  y: "+ y);
	list_texts.forEach( function(text_el, i){
		if(i == 0){
			text_+=text_el;
		}else{
			text_+=cr_lf+text_el;
		}
		//console.log(i+") " + text_);
	});
	text_ = "^FO"+x+","+y+"\n^BQ,2,6" + zpl_text_with_field_separator_qr(text_)
	return text_;
}

function zpl_barcode_from_text(text_){
	return "^BC"+zpl_text_with_field_separator(text_);
}

function zpl_barcode_from_text_x_y(text_,x,y, height){
	return "^BY2,2,"+height+""+zpl_field_origin(x,y)+zpl_barcode_from_text(text_,x,y)+"\n";
}

function zpl_barcode_from_text_x_y_4_2(text_,x,y, height){
	return "^BY4,2,"+height+""+zpl_field_origin(x,y)+zpl_barcode_from_text(text_,x,y)+"\n";
}

function create_zpl_code(data_){
	text_data = "";
	x = 200
	y = 50 
    // Company and clients
	text_data = format_start + create_title(data_.company, data_.client,x,y);
	// lines
	x = 50;
	y = 160;
	text_data += zpl_line(x,y, 700, 3);
    // No. Lote and Date 
	y += 20
	text_ = "Lote: " + data.n_lote + " - Fecha: " + data_.t_start.toLocaleString()//.toLocaleDateString()//.toDateString();
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
    // Worker information: name and id
	text_ = "Worker: " +data_.id_worker + ", " + data_.name_worker;
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	// modelo, color, peso, contenedor
	text_ = "Mixture Info:";
	x = 300
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	text_ = "Color Code: " + data_.color_code + " -- Name: " + data_.color_name;
	x = 60
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	text_ = "Container: " + data_.container + " -- Weight: " + data_.weight+data_.type_w;
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	// Componentes y cantidades
	text_ = "Components:";
	x = 300
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	x = 50;
	y+=10;
	components = data_.components;
	components.forEach( function(comp){
		text_ = "" + comp.component_type + " -- " + comp.component + " -- weight: " + comp.weight+comp.type_w;
		y += 50;
		text_data += zpl_FieldData_font(text_, x,y,"A",30);
		// console.log(comp);
	})
    // QR (Num_Lote, formula/color, peso_total)
	y += 30;
	x = 200;
	list_texts = [];
	list_texts.push("lote: "+data_.n_lote);
	list_texts.push("weight: "+data_.weight+data_.type_w);
	list_texts.push("color_code: "+data_.color_code);
	list_texts.push("id_w: "+data_.id_worker);
	list_texts.push("model: "+data_.model);
	list_texts.push("components: ");
	components.forEach( function(comp){
		text_ = comp.component_type + " - " + comp.component + " - " + comp.weight+comp.type_w;
		list_texts.push(text_);
	})
	text_data += zpl_qr_from_list(list_texts,x,y);
	//y += 50*(list_texts.length); // será diferente tamaño ... 
	// end .... 
	text_data += format_end

	return text_data;
}

var example_created = false;



function sendExampleToPrinter(){
	if(example_created){
		console.log("ENVIANDO A IMPRIMIR!!!");
		writeToSelectedPrinter(code_zpl);
	}
}

////// ************************************************************************ Código de barras de trabajadores
var code_zpl_w = ""; 
list_w = [
	{
		"id": 0,
		"payroll_number": 121,
		"name": "Heber Ramirez Carrera",
		"job_position": 0
	},
	{
		"id": 1,
		"payroll_number": 147,
		"name": "Jose Carlos Vargas Cruz",
		"job_position": 2
	},
	{
		"id": 2,
		"payroll_number": 191,
		"name": "Roberto Alomar Dominguez Calderon",
		"job_position": 1
	},
	{
		"id": 3,
		"payroll_number": 129,
		"name": "Javier Aguirre Rangel",
		"job_position": 3
	},
	{
		"id": 4,
		"payroll_number": 125,
		"name": "Ricardo Rey Rocha",
		"job_position": 2
	},
	{
		"id": 5,
		"payroll_number": 138,
		"name": "Franciso Ruiz Segundo",
		"job_position": 1
	},
	{
		"id": 6,
		"payroll_number": 472,
		"name": "Armando Sanchez Suarez",
		"job_position": 1
	},
	{
		"id": 7,
		"payroll_number": 47,
		"name": "Elena de la Soledad Almaguer Benitez",
		"job_position": 2
	},
	{
		"id": 8,
		"payroll_number": 24,
		"name": "Anahi Celaya",
		"job_position": 2
	}
];

list_post = [
	{
		"id": 0,
		"name": "Assistant Manager",
		"description": ""
	},
	{
		"id": 1,
		"name": "Group Leader",
		"description": ""
	},
	{
		"id": 2,
		"name": "Team Leader",
		"description": ""
	},
	{
		"id": 3,
		"name": "Jr. Team Leader",
		"description": ""
	}
]

function create_barcodes_workers(){
	// Crear códigos de barras de lo que se usara en el proyecto para los trabajadores
	code_zpl_w = "";
	x = 100;
	y = 60;
	code_zpl_w = format_start + "\n" + zpl_FieldData("Codigos Trabajadores (Pruebas):",x,y )+"\n";
	// ----
	x = 30;
	y += 60;
	height_ = 70; 
	spaces = 70;
	list_w.forEach( function(worker_, i){
		position_w = list_post[worker_.job_position].name
		worker_full_name = worker_.name.split(" ");
		info_ = "id: " + worker_.id + "   #: " + worker_.payroll_number + "    Name: " + worker_.name + "   Position: " + position_w;
		text_ = ""+worker_full_name[0] +" "+ position_w +" "+ worker_.payroll_number;
		console.log("Trabajador: " + info_);
		code_zpl_w += zpl_barcode_from_text_x_y(text_,x,y, height_);
		y += height_ + spaces;
	} );

	/// .... end ... 
	code_zpl_w += format_end;

	const p = document.getElementById('code_zpl');
	p.innerText = code_zpl_w;

	console.log(code_zpl_w);
	code_zpl = code_zpl_w;
	example_created = true;
}

////// ************************************************************************ Código de barras de contenedores
var code_zpl_c = ""; 
list_barcodes_containers = ["123423","234112","131307","001204","000001","187932", "202207", "220713", "150722", "130513"]

var multi_labels_barcode = false;
// var code_zpl_qr_comp = ""; 
list_code_zpl = [];

function create_barcodes_containers(){
	num_labels_by_label = 5;
	num_labels = parseInt(list_barcodes_containers.length/num_labels_by_label);
	offset_labels = parseInt(list_barcodes_containers.length%num_labels_by_label);
	list_code_zpl = [];
	height_text_label = 30;
	height_barcode_label = 100;
	spaces = 75;
	if(offset_labels != 0){
		num_labels++;
	}
	if(num_labels > 0){
		j = 0;
		text_code_zpl = "";
		console.log('Num Etiquetas de Contenedores: ' + list_barcodes_containers.length);
		for(k = 0; k < num_labels; k++){
			x = 150; 
			y = 50;
			code_zpl_tmp = format_start + "\n";
			code_zpl_tmp += zpl_FieldData("Codigos de Contenedores (Pruebas):",x,y )+"\n";
			/// ..... all the data for the QRs ....
			x = 200;
			y += 70;
			num_labels_in_label =  k == num_labels - 1 && offset_labels != 0 ? offset_labels : num_labels_by_label;
			for(i = 0; i < num_labels_in_label; i++){
				text_ = ""+list_barcodes_containers[j];
				code_zpl_tmp += zpl_barcode_from_text_x_y_4_2(text_,x,y, height_barcode_label);
				y += height_barcode_label + spaces;
				j++;
			}
			/// ..... end .... 
			code_zpl_tmp += format_end;
			console.log(code_zpl_tmp);
			/// ...... save data 
			list_code_zpl.push(code_zpl_tmp)
			text_code_zpl += "Codigo Seccion "+ k +": \n";
			text_code_zpl += code_zpl_tmp+"\n\n";
		}
		const p = document.getElementById('code_zpl');
		p.innerText = text_code_zpl;
		code_zpl = list_code_zpl[0];
		multi_lables_qr_comp = false;
		multi_labels_barcode = true;

		var select = document.getElementById("arr")
		for ( i = 0; i < list_code_zpl.length; i++) {
            var el = document.createElement("option");
            el.textContent = "Etiqueta " + (i + 1);
            el.value = i;
            select.appendChild(el);
		}
	}else{
		alert('No hay información que formatear');
	}
}



////// ************************************************************************ Código QR de componentes

list_comp = [
	{
		"info_given_by_client":{
			"1": "Solvente",
			"2": "901-6J",
			"3":"L-25"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "9016J.0000.0.006",
			"3": "0025",
			"4": "5",
			"5": "kg",
			"6": "02.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "Solvente",
			"2": "901-B9",
			"3":"L-29"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "901B9.0000.0.006",
			"3": "0029",
			"4": "5",
			"5": "kg",
			"6": "09.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "Catalizador",
			"2": "405-96",
			"3":"L-69"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "40596.0000.0.002",
			"3": "0069",
			"4": "6",
			"5": "kg",
			"6": "09.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "Solvente",
			"2": "901-B9",
			"3": "L-24"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "901B9.0000.0.006",
			"3": "0024",
			"4": "5",
			"5": "kg",
			"6": "02.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4011M.053LN.1.556",
			"3":"L20"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4611M.53LN.1.556",
			"3": "0020",
			"4": "15",
			"5": "kg",
			"6": "10.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.9MJM.7.556",
			"3":"L-9"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.9MJM.7.556",
			"3": "0009",
			"4": "15",
			"5": "kg",
			"6": "02.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "Catalizador",
			"2": "405-96",
			"3":"L-71"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "40596.0000.0.002",
			"3": "0071",
			"4": "6",
			"5": "kg",
			"6": "11.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.2958.7.556",
			"3":""
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.2958.7.556",
			"3": "0006",
			"4": "15",
			"5": "kg",
			"6": "02.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "Catalizador",
			"2": "405-50",
			"3":"L-1403"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "40550.0000.0.559",
			"3": "1403",
			"4": "20",
			"5": "kg",
			"6": "05.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4611M.59CB.1.011",
			"3":""
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4611M.59CB.1.011",
			"3": "0011",
			"4": "25",
			"5": "kg",
			"6": "11.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "A4611M.53LN.1.556",
			"3":"L-19"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4611M.53LN.1.556",
			"3": "0019",
			"4": "15",
			"5": "kg",
			"6": "09.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "Catalizador",
			"2": "405-50",
			"3":"L-1436"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "40550.0000.0.559",
			"3": "1436",
			"4": "20",
			"5": "kg",
			"6": "08.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.99V7.1.556",
			"3":"L14"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.99V7.1.556",
			"3": "0014",
			"4": "15",
			"5": "kg",
			"6": "02.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4601G.0000.9.011",
			"3":"L-28"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4601G.0000.9.011",
			"3": "0028",
			"4": "25",
			"5": "kg",
			"6": "12.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.9MJM.7.556",
			"3":"L-8"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.9MJM.7.556",
			"3": "0008",
			"4": "15",
			"5": "kg",
			"6": "12.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "Solvente",
			"2": "901-86",
			"3":"L-1097"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "90186.0000.0.556",
			"3": "1097",
			"4": "15",
			"5": "kg",
			"6": "05.2024"
		}
	},
	{
		"info_given_by_client":{
			"1": "Solvente",
			"2": "903-89",
			"3":"L-135"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "90389.0000.0.556",
			"3": "0135",
			"4": "15",
			"5": "kg",
			"6": "08.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.9MFS.1.556",
			"3":"L-12"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.9MFS.1.556",
			"3": "0012",
			"4": "15",
			"5": "kg",
			"6": "03.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "LN245",
			"3":"L-1"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "LN245.0009.6.000",
			"3": "0001",
			"4": "0",
			"5": "",
			"6": "12.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "4613P.2958.7.556",
			"3":"L-5"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "4613P.2958.7.556",
			"3": "0005",
			"4": "15",
			"5": "kg",
			"6": "01.2023"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "900-19",
			"3":"L-5"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "90019.0000.0.004",
			"3": "0005",
			"4": "1",
			"5": "GAL",
			"6": "06.2020"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "460SR.90ZC.M.011",
			"3":"L-29"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "460SR.90ZC.M.011",
			"3": "0029",
			"4": "25",
			"5": "kg",
			"6": "10.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "460SR.90ZC.M.011",
			"3":"L-28"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "460SR.90ZC.M.011",
			"3": "0028",
			"4": "25",
			"5": "kg",
			"6": "10.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "460SR.90ZC.M.011",
			"3":"L-40"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "460SR.90ZC.M.011",
			"3": "0040",
			"4": "25",
			"5": "kg",
			"6": "12.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "460SR.90ZC.M.011",
			"3":"L-41"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "460SR.90ZC.M.011",
			"3": "0041",
			"4": "25",
			"5": "kg",
			"6": "12.2022"
		}
	},
	{
		"info_given_by_client":{
			"1": "",
			"2": "460SR.90ZC.M.011",
			"3":"L-43"
		},
		"inf_from_qr":{
			"1": "Mankiewicz",
			"2": "460SR.90ZC.M.011",
			"3": "0043",
			"4": "25",
			"5": "kg",
			"6": "12.2022"
		}
	}
]

var multi_lables_qr_comp = false;
var code_zpl_qr_comp = ""; 
//list_code_zpl = [];
function create_qr_components(){
	num_labels_by_label = 8;
	num_labels = parseInt(list_comp.length/num_labels_by_label);
	offset_labels = parseInt(list_comp.length%num_labels_by_label);
	list_code_zpl = [];
	height_text_label = 30;
	if(offset_labels != 0){
		num_labels++;
	}
	if(num_labels > 0){
		j = 0;
		text_code_zpl = "";
		console.log('Num Components: ' + list_comp.length);
		for(k = 0; k < num_labels; k++){
			x = 200; 
			y = 50;
			code_zpl_tmp = format_start + "\n";
			code_zpl_tmp += zpl_FieldData("Codigos Componetes (Pruebas):",x,y )+"\n";
			/// ..... all the data for the QRs ....
			//x = 20;
			y += 50;
			num_labels_in_label =  k == num_labels - 1 && offset_labels != 0 ? offset_labels : num_labels_by_label ;
			for(i = 0; i < num_labels_in_label; i++){
				data_to_process = list_comp[j].inf_from_qr;
				data_to_label = list_comp[j].info_given_by_client
				list_text = [];
				for( key_ in data_to_process){
					list_text.push(data_to_process[key_]);
				}
				x = i%2 == 0 ? 40 : 420;
				console.log(list_text);
				// name
				code_zpl_tmp += zpl_FieldData_font(data_to_label["2"], x,y,"A",height_text_label);
				y += height_text_label;
				// info to QR 
				code_zpl_tmp += zpl_qr_from_list_2(list_text,x,y);
				//code_zpl_tmp += zpl_qr_from_list(list_text,x,y);
				j++;
				y =  i%2 ? y+200 : y;
			}
			/// ..... end .... 
			code_zpl_tmp += format_end;
			console.log(code_zpl_tmp);
			/// ...... save data 
			list_code_zpl.push(code_zpl_tmp)
			text_code_zpl += "Codigo Seccion "+ k +": \n";
			text_code_zpl += code_zpl_tmp+"\n\n";
		}
		const p = document.getElementById('code_zpl');
		p.innerText = text_code_zpl;
		code_zpl = list_code_zpl[0];
		multi_lables_qr_comp = true;
		multi_labels_barcode = false;

		var select = document.getElementById("arr")
		for ( i = 0; i < list_code_zpl.length; i++) {
            var el = document.createElement("option");
            el.textContent = "Etiqueta " + (i + 1);
            el.value = i;
            select.appendChild(el);
		}
	}else{
		alert('No hay información que formatear');
	}
	
}

function pint_selected_label(){
	if(multi_lables_qr_comp){
		var e = document.getElementById("arr");
		var opt_code_zpl = e.value;
		const p = document.getElementById('code_zpl');
		code_zpl = list_code_zpl[opt_code_zpl];
		p.innerText = code_zpl;
		example_created = true;
		sendExampleToPrinter();
	}else{
		if(multi_labels_barcode){
			var e = document.getElementById("arr");
			var opt_code_zpl = e.value;
			const p = document.getElementById('code_zpl');
			code_zpl = list_code_zpl[opt_code_zpl];
			p.innerText = code_zpl;
			example_created = true;
			sendExampleToPrinter();
		}
	}
	
}

////// ************************************************************************ Código QR de Trabajadores
var code_zpl_qr_w = ""; 
function create_qr_workers(){
	num_labels_by_label = 4;
	num_labels = parseInt(list_w.length/num_labels_by_label);
	offset_labels = parseInt(list_w.length%num_labels_by_label);
	list_code_zpl = [];
	height_ = 170; 
	height_text_label = 30;
	spaces = 70;
	if(offset_labels != 0){
		num_labels++;
	}
	if(num_labels > 0){
		j = 0;
		text_code_zpl = "";
		console.log('Num Trabajadores: ' + list_w.length);
		for(k = 0; k < num_labels; k++){
			x = 100; 
			y = 20;
			code_zpl_tmp = format_start + "\n";
			code_zpl_tmp += zpl_FieldData("Codigos QR Trabjaadores (Pruebas):",x,y )+"\n";
			/// ..... all the data for the QRs ....
			//x = 20;
			y += 60;
			num_labels_in_label =  k == num_labels - 1 && offset_labels != 0 ? offset_labels : num_labels_by_label ;
			for(i = 0; i < num_labels_in_label; i++){
				worker_ = list_w[j]; 
				position_w = list_post[worker_.job_position].name
				list_text = [worker_.payroll_number, worker_.name, position_w];
				info_ = "id: " + worker_.id + "   #: " + worker_.payroll_number + "    Name: " + worker_.name + "   Position: " + position_w;
				// name
				//x = 300
				code_zpl_tmp += zpl_FieldData_font(worker_.name, x,y,"A",height_text_label);
				y += height_text_label;
				// ---- 
				console.log("Trabajador: " + info_);
				code_zpl_tmp += zpl_qr_from_list(list_text,x,y);
				y += height_ + spaces;
				j++;
			} 
			// ..... end .... 
			code_zpl_tmp += format_end;
			console.log(code_zpl_tmp);
			/// ...... save data 
			list_code_zpl.push(code_zpl_tmp)
			text_code_zpl += "Codigo Seccion "+ k +": \n";
			text_code_zpl += code_zpl_tmp+"\n\n";
		}
		const p = document.getElementById('code_zpl');
		p.innerText = text_code_zpl;
		code_zpl = list_code_zpl[0];
		multi_lables_qr_comp = true;

		var select = document.getElementById("arr")
		for ( i = 0; i < list_code_zpl.length; i++) {
            var el = document.createElement("option");
            el.textContent = "Etiqueta " + (i + 1);
            el.value = i;
            select.appendChild(el);
		}
	}else{
		alert('No hay información que formatear');
	}
	/*
	//// --- 
	code_zpl_qr_w = format_start + "\n";
	/// ..... all the data for the QR ....
	x = 100;
	y = 60;
	code_zpl_qr_w = format_start + "\n" + zpl_FieldData("Codigos Trabajadores (Pruebas):",x,y )+"\n";
	// ----
	x = 300;
	y += 60;
	height_ = 150; 
	height_text_label = 30;
	spaces = 70;
	list_w.forEach( function(worker_, i){
		position_w = list_post[worker_.job_position].name
		list_text = [worker_.payroll_number, worker_.name, position_w];
		info_ = "id: " + worker_.id + "   #: " + worker_.payroll_number + "    Name: " + worker_.name + "   Position: " + position_w;
		// name
		//x = 300
		code_zpl_qr_w += zpl_FieldData_font(worker_.name, x,y,"A",height_text_label);
		y += height_text_label;
		// ---- 
		console.log("Trabajador: " + info_);
		code_zpl_qr_w += zpl_qr_from_list(list_text,x,y);
		y += height_ + spaces;
	} );
	
	/// ..... end .... 
	code_zpl_qr_w += format_end;
	console.log(code_zpl_qr_w);
	const p = document.getElementById('code_zpl');
	p.innerText = code_zpl_qr_w;

	code_zpl = code_zpl_qr_w;
	example_created = true;
	*/
}


function promptFile(contentType, multiple) {
	var input = document.createElement("input");
	input.type = "file";
	input.multiple = multiple;
	input.accept = contentType;
	return new Promise(function(resolve) {
		document.activeElement.onfocus = function() {
		document.activeElement.onfocus = null;
		setTimeout(resolve, 500);
		};
		input.onchange = function() {
		var files = Array.from(input.files);
		if (multiple)
			return resolve(files);
		resolve(files[0]);
		};
		input.click();
	});
}

function promptFilename() {
	promptFile().then(function(file) {
		document.querySelector("#span1").innerText = file && file.name || "no file selected";
	});
}

function sendFile2Print(){
	console.log("ENTOR!")
	file_text = document.querySelector("#span1").innerText
	console.log(file_text)
	// sendFile('ejemplo1.zpl');
}
