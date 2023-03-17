var initial_info = JSON.parse(localStorage.getItem('initial_info'))
var mixProcess = JSON.parse(localStorage.getItem('mixProcess'))
var components_formula = JSON.parse(localStorage.getItem('components_formula'))
var mixContainer = JSON.parse(localStorage.getItem(`mixContainer-${btn_index_Container}`))
var actual_container = localStorage.getItem('actual_container')
var containers_number = localStorage.getItem('num_containers')
let id_container_ = parseInt(localStorage.getItem('id_component'))
var temperatura = "" // poner dos cifras decimales 
var humedad = "" // poner dos cifras decimales 
var viscosidad = "" // poner dos cifras decimales 

let machine = undefined

console.log("Initial Value",initial_info)
console.log("MixProces",mixProcess)
console.log("Comp Formula",components_formula)
console.log("Mix Container",mixContainer)

var selected_device;
var devices = [];

struct_save_zpl = {
	'id' : 0,
	'zpl_code' : "",
	'creation_date' : "",
	"update_date" : ""
}

function setup() {
	console.log("entro setupt!!")
	//Get the default device from the application as a first step. Discovery takes longer to complete.
	BrowserPrint.getDefaultDevice("printer", function(device) {
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

function sendImage(imageUrl)
{
	url = window.location.href.substring(0, window.location.href.lastIndexOf("/"));
	url = url + "/" + imageUrl;
	selected_device.convertAndSendFile(url, undefined, errorCallback)
}
function sendFile(fileUrl){
    url = window.location.href.substring(0, window.location.href.lastIndexOf("/"));
    url = url + "/" + fileUrl;
    selected_device.sendFile(url, undefined, errorCallback)
}
function onDeviceSelected(selected)
{
	/* for(var i = 0; i < devices.length; ++i){
		console.log("Num. Dispositivos:",devices.length)
		if(selected.value == devices[i].uid)
		{
			selected_device = devices[i];
			return;
		}
	} */

	selected_device = devices[0]
}

////// ----------------------------------------- 

var code_zpl = "";

var format_start = "^XA^LL200^FO80,50^A0N36,36^FD";
var format_end = "^FS^XZ";
var field_origin = "^FO";
var field_data = "^FD";
var title_height = 60;
var font_title = "0";
var field_separator="^FS";

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

function zpl_FieldData(text,x,y){
    return field_origin+x+","+y+zpl_text_with_field_separator(text)+"\n";
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

async function create_zpl_code(){
	//setup()
	await get_machine_info()
	machine = identifie_response.record.id_in
	components_formula = JSON.parse(localStorage.getItem('components_formula'))
	mixContainer = JSON.parse(localStorage.getItem(`mixContainer-${btn_index_Container}`))
	console.log(mixContainer)
	console.log(components_formula)
	onDeviceSelected()
	console.log(selected_device) 
	//return;
	if(typeof(selected_device) == 'undefined'){
		alert('La impresora no esta conectada. Verificar conexión')
	} else{
		localStorage.removeItem('actual_container')
		$('#reportModal').modal('hide')
		$('#removePaintModal').modal('show')
	}	

	text_data = "";
	x = 200
	y = 50 
    // Company and clients
	text_data = format_start + create_title('Moriroku Technology', initial_info.client_name,x,y);
	// lines
	x = 50;
	y = 160;
	text_data += zpl_line(x,y, 700, 3);
    // No. Lote and Date 
	y += 20                                   //fecha de finalización del mezclado del contenedor
	text_ = "Lote: " + machine + "-" + initial_info.n_lote + " - Fecha: " + mixContainer.t_end.toLocaleString()//.toLocaleDateString()//.toDateString();
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
    // Worker information: name and id
	text_ = "Worker: " +mixProcess.id_worker + ", " + mixProcess.name_worker;
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	// modelo, color, peso, contenedor
	text_ = "Mixture Info:";
	x = 300
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	text_ = "Color Code: " + initial_info.color_code + " -- Name: " + initial_info.color_name;
	x = 60
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	text_ = "Container: " + actual_container + "/" + containers_number + " -- W: " + parseInt(mixContainer.weight).toFixed(0)+'g';
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	// Componentes y cantidades
	text_ = "Components:";
	x = 300
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
	x = 50;
	y+=10;

	components_formula.forEach( function(comp){
		text_ = "" + comp.type_compent_name + " -- " + comp.comp_name + " -- w: " + comp.weight+'g';
		y += 50;
		text_data += zpl_FieldData_font(text_, x,y,"A",30);
		// console.log(comp);
	})
	// ------- temperatura, humedad y viscosidad ..... 
	text_ = "T: " + mixContainer.temperature + " -- H: " + mixContainer.humidity + " -- V: " + mixContainer.viscosity;
	y += 50;
	text_data += zpl_FieldData_font(text_, x,y,"A",30);
    // QR (Num_Lote, formula/color, peso_total)
	y += 30;
	x = 200;
	list_texts = [];
	list_texts.push("l=" + machine + "-" +initial_info.n_lote);
	list_texts.push("b=" + id_container_); //FALTA PROBAR EN PRODUCCIÓN
	list_texts.push("f="+mixContainer.t_end.toLocaleString()); //fecha de finalización del mezclado del contenedor
	list_texts.push("e="+mixProcess.id_worker);
	list_texts.push("c="+initial_info.color_code);
	list_texts.push("w="+parseInt(mixContainer.weight).toFixed(0)+'g');
	list_texts.push("m="+initial_info.model);
	list_texts.push("r="+mixContainer.rework);
	text_info_comp = "i="
	components_formula.forEach( function(comp){
		//text_ = "" + comp.type_compent_name + " - " + comp.comp_name + " - weight: " + comp.weight+'g';
		text_info_comp += comp.type_compent_name + "," + comp.comp_name + "," + parseInt(comp.weight).toFixed(0)+'g';
		//list_texts.push(text_);
		if(components_formula[components_formula.length - 1].name != comp.name ){ //Checar que la comparación de los nombres 
			text_info_comp +=":";
		}
	})
	list_texts.push(text_info_comp);
	text_data += zpl_qr_from_list(list_texts,x,y);
	//y += 50*(list_texts.length); // será diferente tamaño ... 
	// end .... 
	text_data += format_end
	code_zpl = text_data;
	writeToSelectedPrinter(code_zpl)

	struct_save_zpl['id'] = id_component //mixContainer.id
	struct_save_zpl['zpl_code'] = code_zpl
	//Cambiar ruta y la estructura struct_save_zpl
	await post_zpl_code(struct_save_zpl)
	//debugger
	console.log(api_response.data.rest)
	console.log(code_zpl)
	
}


$('#removePaintModal').on('show.bs.modal', () => {
	const timer = 4000
	setTimeout(() => {
		$('#removePaintModal').modal('hide')        
		window.location.replace('/mixing/containers')
	},timer)
})