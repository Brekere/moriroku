const RAPIDAPI_API_URL = 'http://localhost:5000/api/';
        var api_response;
        const RAPIDAPI_REQUEST_HEADERS = {
            'X-RapidAPI-Host': 'arjunkomath-jaas-json-as-a-service-v1.p.rapidapi.com'
            , 'X-RapidAPI-Key': '7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            , 'Content-Type': 'application/json'
        };
        async function get_from_api(url_, data){
            await axios.get(url_, data).then(response => {        
                console.log(response);
                api_response = response.data
        }).catch(error => console.error('On get student error', error))
        }

        async function post_to_api(url_, data){
            await axios.post(url_, data).then(response => {
                console.log(response);
                api_response = response
        }).catch(error => console.error('On get student error', error))
        }
        ///////

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