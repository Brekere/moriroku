const RAPIDAPI_API_URL = 'http://localhost:5055/api/';
//const RAPIDAPI_API_URL_POST = 'http://localhost:5055/api/create/';
//const RAPIDAPI_API_URL_GET = 'http://localhost:5055/api/get/';
const RAPIDAPI_REQUEST_HEADERS = {
    'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
    , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    , 'Content-Type': 'application/json'
};

function get_from_api(url_, data){
    axios.get(url_, data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
}

function post_to_api(url_, data){
    axios.post(url_, data).then(response => {
        console.log(response);
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

function get_process_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
    /*
    console.log(data);
    axios.get(`${RAPIDAPI_API_URL}`+'processes', data).then(response => {
        console.log(response);
  }).catch(error => console.error('On get student error', error))
  */
}

function post_process(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
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

function get_container_by_id(id_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {id: id_} };
    get_from_api(url_, data);
}

function post_container(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
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

function post_component_tare(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_tare';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
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

function post_component_viscosity_improvement(data_){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'component_viscosity_improvement';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {"record": data_} };
    post_to_api(url_, data)
}

