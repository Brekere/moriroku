
const RAPIDAPI_API_URL = 'http://localhost:5000/';
const RAPIDAPI_REQUEST_HEADERS = {
  'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
  , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  , 'Content-Type': 'application/json'
};

var opcion;

function init_tare(port_){
    //console.log('Hola: ' + port_);
    axios.get(`${RAPIDAPI_API_URL}`+'init_tare/'+port_, { headers: RAPIDAPI_REQUEST_HEADERS }).then(response => {
    console.log('work: ' + response.data['work'] + '    Resultado: ' + response.data['result']);
  }).catch(error => console.error('On get student error', error))
  }

function get_weight(port_){
    //console.log('Hola: ' + port_);
    axios.get(`${RAPIDAPI_API_URL}`+'get_weights/'+port_, { headers: RAPIDAPI_REQUEST_HEADERS }).then(response => {
    //console.log('peso: ' + response.data['weight'] + '    Tipo: ' + response.data['type']);
    if(opcion == 0){
      update_weight_page(response.data['weight'], response.data['type'])
    }else{
      factor = 1;
      if(response.data['type'].includes("kg")){
        factor = 1000;
      }
      update_level_from_data(parseFloat(response.data['weight'])*factor)
    }
    
  }).catch(error => console.error('On get student error', error))
  }

function update_weight_page(weight_, type_w){
  //console.log('Actualizando ----> peso: ' + weight_ + '    Tipo: ' + type_w)
  var elem_w = document.getElementById('Weight');
   elem_w.value = weight_;
   var elem_tw = document.getElementById('Type_w');
   elem_tw.value = type_w;
}


