/* const RAPIDAPI_API_URL = 'http://localhost:5000/api/'; */
var api_response = undefined
var identifie_response = undefined
/* const RAPIDAPI_REQUEST_HEADERS = {
    'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
    , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    , 'Content-Type': 'application/json'
}; */

async function get_from_api(url_, data){
    await axios.get(url_, data).then(response => {        
        console.log(response);
        identifie_response = response.data
  }).catch(error => console.error('On get student error', error))
}

async function post_to_api(url_, data){
    await axios.post(url_, data).then(response => {
        console.log(response);
        api_response = response
  }).catch(error => console.error('On get student error', error))
}

// --------------------- Mix Process

function get_all_process(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
    /*
    console.log(data);
    axios.get(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

async function get_process_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    await get_from_api(url_, data);
    /*
    console.log(data);
    axios.get(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

async function post_process(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
    /*
    console.log(data);
    axios.post(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

async function post_process_errors(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes/errors';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
    /*
    console.log(data);
    axios.post(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

// --------------------- Mix Container

function get_all_container(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
}

async function get_container_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    await get_from_api(url_, data);
}

async function post_container(data_){
    console.log(data_)
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
}

async function post_container_errors(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container/errors';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
    /*
    console.log(data);
    axios.post(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

// --------------------- Viscosity Improvement

function get_all_viscosity_improvement(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
}

function get_viscosity_improvement_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
}

function post_viscosity_improvement(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
}


// --------------------- Process Container Component

function get_all_process_container_component(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'process_container_component';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
}

function get_process_container_component_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'process_container_component';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
}

function post_process_container_component(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'process_container_component';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
}

// --------------------- Component Tare

function get_all_component_tare(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_tare';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
}

function get_component_tare_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_tare';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
}

async function post_component_tare(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_tare';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
}


// --------------------- Component Viscosity Improvement

function get_all_component_viscosity_improvement(){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: -1} };
    get_from_api(url_, data);
}

function get_component_viscosity_improvement_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
}

async function post_component_viscosity_improvement(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
}

async function get_component_identifier(data_){
    console.log('Obtener el Identificador');
    url_ = `${RAPIDAPI_API_URL}`+'get_comp_identifier';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params:  data_ };
    await get_from_api(url_, data)
}

// --------------------- Save ZPL file

async function get_zpl_code(id_){
    console.log('Obtener el codigo ZPL');
    url_ = `${RAPIDAPI_API_URL}`+'container_label';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    await get_from_api(url_, data);
}

async function post_zpl_code(data_){
    console.log('Guardar el codigo ZPL');
    url_ = `${RAPIDAPI_API_URL}`+'container_label';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
}

// --------------------- Obtencion Info Maquina

async function get_machine_info(){
    console.log('Obtener el codigo ZPL');
    url_ = `${RAPIDAPI_API_URL}`+'machine_info';
    data = { headers: RAPIDAPI_REQUEST_HEADERS };
    await get_from_api(url_, data);
}

// --------------------- Obtencion Info Maquina

async function post_process_step_release(data_){
    console.log('Guardar el codigo ZPL');
    url_ = `${RAPIDAPI_API_URL}`+'process_step_release';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    await post_to_api(url_, data)
}

// --------------------- Liberación de sustancia por Departamento

async function post_register_departament(data_){
    url_ = `${RAPIDAPI_API_URL}`+ 'register'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record" : data_} }
    await post_to_api(url_, data)
}

async function post_auth_departament(data_){
    url_ = `${RAPIDAPI_API_URL}` + 'validate_departament'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_}}
    await post_to_api(url_, data)
}

// --------------------- Obtención del color por código de color

async function get_color_by_color_code(id_){
    url = `${RAPIDAPI_API_URL}` + 'getColorbyColorCode'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id_color: id_} }
    await get_from_api(url, data)
}

// --------------------- Obtención de información del zpl

async function get_zpl_info_by_id(id_){
    url = `${RAPIDAPI_API_URL}` + 'get_zpl_info'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} }
    await get_from_api(url, data)
}

// --------------------- Obtención de información del zpl

async function get_components_by_colorid(id_){
    url = `${RAPIDAPI_API_URL}` + 'getComponentInfoByContainer'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} }
    await get_from_api(url, data)
}

// --------------------- Obtención de información del zpl

async function get_model_by_id(id_){
    url = `${RAPIDAPI_API_URL}` + 'getModelbyId'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} }
    await get_from_api(url, data)
}

// --------------------- Obtención de información del zpl

async function post_test_zpl(data_){
    console.log(data_)
    url = `${RAPIDAPI_API_URL}` + 'save_zpl'
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} }
    await post_to_api(url, data)
}