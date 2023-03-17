const RAPIDAPI_API_URL_MAIN = 'http://localhost:5000/'; 
/* const RAPIDAPI_REQUEST_HEADERS = {
  'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
  , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  , 'Content-Type': 'application/json'
};
 */
var opcion;
var response_;
var response_tare = true
var detected_error_get_weight = false

/* ----------Falta probar las modificaciones---------- */ 
async function init_tare(port_){
  //console.log('Hola: ' + port_);
  await axios.get(`${RAPIDAPI_API_URL_MAIN}`+'api/init_tare', { headers: RAPIDAPI_REQUEST_HEADERS }).then(response => {
    console.log('work: ' + response.data['work'] + '    Resultado: ' + response.data['rest']);
    response.data['rest'] != 'SUCCESS' ? response_tare = false : response_tare = true
  }).catch(error => {
    console.log('On get student error', error)
    response_tare = false
  })
}

/* ----------Falta probar las modificaciones---------- */ 
function get_weight(port_){
    //console.log('Hola: ' + port_);
    axios.get(`${RAPIDAPI_API_URL_MAIN}`+'api/get_weights', { headers: RAPIDAPI_REQUEST_HEADERS }).then(response => {
    //console.log('peso: ' + response.data['weight'] + '    Tipo: ' + response.data['type']);
    response_ = response
    if(response.data['rest'] == "SUCCESS"){
      if(opcion == 0){
        update_weight_page(response.data['weight'], response.data['type'])
      }else{
        factor = 1;
        if(response.data['type'].includes("kg")){
          factor = 1000;
        }
        update_level_from_data(parseFloat(response.data['weight'])*factor)
      }
      if(detected_error_get_weight == true){
        detected_error_get_weight = false
        $('#warningGraphModal').modal('hide')
      }
    } else {
      if(detected_error_get_weight == false){
        detected_error_get_weight = true
        $('#warningGraphModal').modal('show')
      }
    }
  }).catch(error => {
    console.log('On get student error', error)
    if(detected_error_get_weight == false){
      detected_error_get_weight = true
      $('#warningGraphModal').modal('show')
    }
  })
  }

function update_weight_page(weight_, type_w){
  //console.log('Actualizando ----> peso: ' + weight_ + '    Tipo: ' + type_w)
  var elem_w = document.getElementById('Weight');
   elem_w.value = weight_;
   var elem_tw = document.getElementById('Type_w');
   elem_tw.value = type_w;
}


