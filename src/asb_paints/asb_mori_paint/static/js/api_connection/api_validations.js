const RAPIDAPI_API_URL = 'http://localhost:5000/api/';
var response_data = ""

const RAPIDAPI_REQUEST_HEADERS = {
    'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
    , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    , 'Content-Type': 'application/json'
};

async function get_from_apis(url_, data){
    await axios.get(url_, data).then(response => {
        console.log(response);
        response_data = response.data
        console.log("Respuesta", response_data)
  }).catch(error => console.error('On get student error', error))
}

async function get_worker_byPayNumber(data_worker){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'worker_authentication';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {user_number : data_worker}} 
    console.log(data)
    await get_from_apis(url_, data)
}

async function get_validation_container(barcode_container){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'container_validation';
    data = { headers: RAPIDAPI_REQUEST_HEADERS, params: {barcode_text : barcode_container}}
    await get_from_apis(url_, data)
}

async function get_nextid_proces(num_container){
    console.log('Obtener todos los procesos');
    url_ = `${RAPIDAPI_API_URL}`+'processes/next_id';
    data = { headers: RAPIDAPI_REQUEST_HEADERS}
    await get_from_apis(url_, data)
}