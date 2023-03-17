let language_json = undefined
let wo_detail_language = undefined

let text_title = document.getElementById('title')
let text_lang_drop = document.getElementById('lang_drop')
let text_spanish = document.getElementById('spanish')
let text_english = document.getElementById('english')
let text_title_wo = document.getElementById('title-ot-detail')
let text_subtitle_wo = document.getElementById('subtitle-ot')
let label_wo = document.getElementById('ot-label-')
let leyend_num_lot = document.getElementById('leyend-ot')
let label_date = document.getElementById('date-label')
let label_color = document.getElementById('formula-color')
let place_holder = document.getElementById('select-opt-ph')
let label_model = document.getElementById('model-select')
let label_pieces = document.getElementById('num-pieces')
let label_client_name = document.getElementById('client_name_label')
let label_filter = document.getElementById('filter_label')
let label_lote_name = document.getElementById('lotname_label')

let modal_process_wo = document.getElementById('insertDataModalLabel')
let modal_process_pz = document.getElementById('insertDataModalLabel')

let modal_title_warn_wo = document.getElementById('ensureWOModalLabel')
let modal_body_warn_wo = document.getElementById('message-worker')
let modal_body_warn2_wo = document.getElementById('message-worker-02')
let btn_edit_modal_wo = document.getElementById('edit-wo')
let btn_add_modal_wo = document.getElementById('add-wo')

let modal_title_warn_pz = document.getElementById('ensureContainerModalLabel')
let modal_body_warn1_pz = document.getElementById('message-container')
let modal_body_warn2_pz = document.getElementById('message-container-02')
let btn_edit_modal_pz = document.getElementById('edit-pz')
let btn_add_modal_pz = document.getElementById('add-pz')

let modal_title_info_data = document.getElementById('infoProcessModalLabel')
let modal_subtitle_info_data = document.getElementById('message-worker-info')
let modal_client_info_data = document.getElementById('client-info')
let modal_lot_info_data = document.getElementById('lot-info')
let modal_wo_info_data = document.getElementById('wo_info_')
let modal_filter_info_data = document.getElementById('filter-l-info')
let modal_color_info_data = document.getElementById('color-info')
let modal_model_info_data = document.getElementById('model-l-info')
let modal_pieces_info_data = document.getElementById('pieces-info')
let modal_weight_info_data = document.getElementById('weight-info')

let modal_text_edit = document.getElementById('edit_text')
let modal_text_edit_1 = document.getElementById('edit_text_1')

let modal_error_body_1 = document.getElementById('error-mis-01')
let modal_error_body_2 = document.getElementById('error-mis-02')
let modal_error_body_wo = document.getElementById('error-body-wo')
let modal_error_body_pz = document.getElementById('error-body-pz')

let btn_edit_c_label = document.getElementById('add-WorkOrder')
let btn_edit_p_label = document.getElementById('add-Pieces')
let btn_start_label = document.getElementById('checkInfo')
let btn_start_process_label = document.getElementById('start_process')
let btn_edit_process_label = document.getElementById('edit_process')

let session_strg_list_lang = JSON.parse(sessionStorage.getItem('list_language'))
let session_strg_lang = sessionStorage.getItem('language')

fetch('static/config_json/language.json').then(response => {
    return response = response.json()
}).then( data => {
    language_json = data
})

if(session_strg_lang == 'eng'){    
    changeLanguagePage(session_strg_list_lang)
} else if (session_strg_lang == 'esp'){
    wo_detail_language = session_strg_list_lang.WO_detail
}


function languageSelect(lan){
    list_lang = language_json[0]['list']
    console.log(list_lang)
    console.log(lan)
    lan == 'esp' ? language = 'Spanish' : language = 'English'
    console.log(language)
    for (let index = 0; index < list_lang.length; index++) {
        if(list_lang[index]['language'] == language){
            list_lang = list_lang[index]['esp']        
        } else {
            list_lang = list_lang[index+1]['eng']
        }
    }
    
    sessionStorage.setItem('list_language', JSON.stringify(list_lang))
    sessionStorage.setItem('language', lan)
    changeLanguagePage(list_lang)
}

function changeLanguagePage(list_lang_){
    text_title.textContent = list_lang_.title_nav
    text_lang_drop.textContent = list_lang_.languages
    text_spanish.textContent = list_lang_.spanish
    text_english.textContent = list_lang_.english
    wo_detail_language = list_lang_.WO_detail
    text_title_wo.textContent = wo_detail_language.title
    text_subtitle_wo.textContent = wo_detail_language.subtitle
    label_color.textContent = wo_detail_language.number_wo
    btn_edit_c_label.textContent = wo_detail_language.btn_edit
    btn_edit_p_label.textContent = wo_detail_language.btn_edit
    label_color.textContent = wo_detail_language.formula
    place_holder.textContent = wo_detail_language.option_placeholder
    label_model.textContent = wo_detail_language.model
    label_pieces.textContent = wo_detail_language.quantity
    label_wo.textContent = wo_detail_language.number_wo
    label_date.textContent = wo_detail_language.date_label
    leyend_num_lot.textContent = wo_detail_language.leyend
    label_client_name.textContent = wo_detail_language.client_name
    label_filter.textContent = wo_detail_language.filter
    label_lote_name.textContent = wo_detail_language.num_lot

    modal_process_wo.textContent = wo_detail_language.process_title_wo
    modal_process_pz.textContent = wo_detail_language.process_title_pz

    modal_title_warn_wo.textContent = wo_detail_language.warning_title_wo
    modal_body_warn_wo.textContent = wo_detail_language.warning_body_wo
    modal_body_warn2_wo.textContent = wo_detail_language.warning_body_wo_02
    
    modal_title_warn_pz.textContent = wo_detail_language.warning_title_pz
    modal_body_warn1_pz.textContent = wo_detail_language.warning_body_pz
    modal_body_warn2_pz.textContent = wo_detail_language.warning_body_pz_02

    modal_text_edit.textContent = wo_detail_language.btn_edit
    modal_text_edit_1.textContent = wo_detail_language.btn_edit

    btn_add_modal_wo.textContent = wo_detail_language.btn_add
    btn_edit_modal_wo.textContent = wo_detail_language.btn_edit
    btn_add_modal_pz.textContent = wo_detail_language.btn_add
    btn_edit_modal_pz.textContent = wo_detail_language.btn_edit
    btn_start_label.textContent = wo_detail_language.btn_start
    btn_start_process_label.textContent = wo_detail_language.btn_start
    btn_edit_process_label.textContent = wo_detail_language.btn_edit

    modal_title_info_data.textContent = wo_detail_language.info_title_modal
    modal_subtitle_info_data.textContent = wo_detail_language.info_subt_modal
    modal_client_info_data.textContent = wo_detail_language.client_name
    modal_lot_info_data.textContent = wo_detail_language.num_lot
    modal_wo_info_data.textContent = wo_detail_language.number_wo
    modal_filter_info_data.textContent = wo_detail_language.filter
    modal_color_info_data.textContent = wo_detail_language.formula
    modal_model_info_data.textContent = wo_detail_language.model_info
    modal_pieces_info_data.textContent = wo_detail_language.quantity

    modal_error_body_1.textContent = wo_detail_language.error_body_mis_01
    modal_error_body_2.textContent = wo_detail_language.error_body_mis_02
    modal_error_body_wo.textContent = wo_detail_language.error_body_wo
    modal_error_body_pz.textContent = wo_detail_language.error_body_pz
}