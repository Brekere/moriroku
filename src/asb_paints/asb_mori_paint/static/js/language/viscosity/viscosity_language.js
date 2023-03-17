let language_json = undefined
let viscosity_language = undefined
let improved_mix = undefined

let header_title = document.getElementById('title')
let header_language = document.getElementById('lang_drop')
let header_language_spanish = document.getElementById('spanish')
let header_language_englisg = document.getElementById('english')

let label_barcode_title = document.getElementById('barcode')
let label_humidity = document.getElementById('humidity_label')
let label_viscosity = document.getElementById('viscosity_label')
let label_temperature = document.getElementById('temperature_label')
let label_date_r = document.getElementById('date_label')
let label_lot_r = document.getElementById('lot_label')
let label_operator_r = document.getElementById('operator_label')
let label_colorcode_r = document.getElementById('colorcode_label')
let label_weight_r = document.getElementById('weight_label')
let label_container_r = document.getElementById('container_label')
let label_colorname_r = document.getElementById('colorname_label')

let modal_scan_title = document.getElementById('improvedCheckModalLabel')
let modal_start_title = document.getElementById('improvedcontainerModalLabel')
let modal_calibration_title = document.getElementById('improvedcalinModalLabel')
let modal_graph_title = document.getElementById('substance_v')
let modal_timer_title = document.getElementById('timerImproveModalLabel')
let modal_info_title = document.getElementById('temperatureImproveModalLabel')
let modal_report_title = document.getElementById('reportModalLabel')

let modal_subtitle_report_mix = document.getElementById('info_mix')
let modal_subtitle_report_comp = document.getElementById('components')
let modal_subtitle_graph = document.getElementById('weight_exp_l')

let modal_info_body = document.getElementById('body_temperature_moda')
let modal_start_body = document.getElementById('improved_start_container')
let modal_calibration_body = document.getElementById('body_calibration')
let modal_scan_body1 = document.getElementById('body_scan_01')
let modal_scan_body2 = document.getElementById('body_scan_02')

let modal_warn_title_t = document.getElementById('ensureContainerModalLabel')
let modal_warn_title_h = document.getElementById('ensureHumModalLabel')
let modal_warn_title_v = document.getElementById('viscoInfoModalLabel')

let modal_body_warn_t = document.getElementById('temp_warn_01')
let modal_body_warn_v = document.getElementById('visco_warn_01')
let modal_body_warn_h = document.getElementById('hum_warn_01')
let modal_warn_body_2 = document.querySelectorAll('#body_warning_2')

let btn_start_substance = document.getElementById('start_substance')
let btn_finish = document.getElementById('btn-finish')
let btn_add_temperature = document.getElementById('button-temperature')
let btn_add_humidity = document.getElementById('button-humidity')
let btn_add_viscosity = document.getElementById('button-viscosity')
let btn_print = document.getElementById('print')
let btn_ready = document.getElementById('ready_btn')
let btn_close_1 = document.querySelectorAll('#btn-close')
let btn_graph_subs = document.getElementById('readySubsatance')
let btn_graph_combi = document.getElementById('readyCombination')
let btn_accept = document.querySelectorAll('#btn_accept')
let btn_edit = document.querySelectorAll('#btn_edit')

let modal_error_title_tare = document.getElementById('errorTareModalLabel')

let modal_error_body_blank = document.getElementById('error_blank')
let modal_error_body_camp = document.getElementById('camp')
let modal_error_body_camp_2 = document.getElementById('camp_body_2')
let modal_error_body_temp = document.getElementById('temperature_error_cel')
let modal_error_body_visco = document.getElementById('viscosity_error_s')
let modal_error_body_humidi = document.getElementById('humidity_error_perc')
let modal_error_body_tare = document.getElementById('tare_body_error')

let session_strg_list_lang = JSON.parse(sessionStorage.getItem('list_language'))
let session_strg_lang = sessionStorage.getItem('language')

fetch('/static/config_json/language.json').then(response => {
    return response = response.json()
}).then( data => {
    language_json = data
})

if(session_strg_lang == 'eng'){
    changeLanguagePage(session_strg_list_lang)
} else {
    improved_mix = session_strg_list_lang.improved_mix
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
    
    console.log(list_lang)
    sessionStorage.setItem('list_language', JSON.stringify(list_lang))
    sessionStorage.setItem('language', lan)
    changeLanguagePage(list_lang) 
}

function changeLanguagePage(list_lang_){
    header_title.textContent = list_lang_.title_nav
    header_language.textContent = list_lang_.languages
    header_language_spanish.textContent = list_lang_.spanish
    header_language_englisg.textContent = list_lang_.english
    
    improved_mix = list_lang_.improved_mix
    
    label_barcode_title.textContent = improved_mix.barcode_label
    label_humidity.textContent = improved_mix.subtitle_modal_hum
    label_viscosity.textContent = improved_mix.subtitle_modal_vis
    label_temperature.textContent = improved_mix.subtitle_modal_tem
    label_date_r.textContent = improved_mix.modal_print_date
    label_lot_r.textContent = improved_mix.modal_print_lot
    label_operator_r.textContent = improved_mix.modal_print_worker
    label_colorcode_r.textContent = improved_mix.modal_print_code_color
    label_weight_r.textContent = improved_mix.modal_print_weight
    label_container_r.textContent = improved_mix.modal_print_container
    label_colorname_r.textContent = improved_mix.modal_print_name_color

    modal_scan_title.textContent = improved_mix.title_modal_scan_comp
    modal_start_title.textContent = improved_mix.title_modal_start_fill
    modal_calibration_title.textContent = improved_mix.title_modal_calibration
    modal_graph_title.textContent = improved_mix.title_modal_graph
    modal_timer_title.textContent = improved_mix.title_modal_temporicer
    modal_info_title.textContent = improved_mix.title_modal_hum
    modal_report_title.textContent = improved_mix.title_modal_print

    modal_subtitle_report_mix.textContent = improved_mix.modal_print_info_mix
    modal_subtitle_report_comp.textContent = improved_mix.modal_print_components
    modal_subtitle_graph.textContent = improved_mix.subtitle_modal_graph
    
    modal_info_body.textContent = improved_mix.body_modal_hum
    modal_start_body.textContent = improved_mix.body_modal_start_fill
    modal_calibration_body.textContent = improved_mix.body_modal_calibration
    modal_scan_body1.textContent = improved_mix.body_1_modal_scan_comp
    modal_scan_body2.textContent = improved_mix.body_2_modal_scan_comp

    modal_warn_title_t.textContent = improved_mix.modal_title_warn_t
    modal_warn_title_h.textContent = improved_mix.modal_title_warn_h
    modal_warn_title_v.textContent = improved_mix.modal_title_warn_v

    modal_body_warn_t.textContent = improved_mix.modal_body_1_warn_t
    modal_body_warn_v.textContent = improved_mix.modal_body_1_warn_v
    modal_body_warn_h.textContent = improved_mix.modal_body_1_warn_h
    modal_warn_body_2.forEach(item => {
        item.textContent = improved_mix.modal_body_warn_02
    })
    
    modal_error_title_tare.textContent = improved_mix.modal_error_connection_title
    
    modal_error_body_tare.textContent = improved_mix.modal_error_connection_body
    modal_error_body_blank.textContent = improved_mix.modal_error_blank
    modal_error_body_camp.textContent = improved_mix.modal_error_blank_info
    modal_error_body_camp_2.textContent = improved_mix.modal_error_blank_info_2
    modal_error_body_temp.textContent = improved_mix.modal_error_temp_body
    modal_error_body_visco.textContent = improved_mix.modal_error_visco_body
    modal_error_body_humidi.textContent = improved_mix.modal_error_humi_body

    btn_start_substance.textContent = improved_mix.btn_start_substance
    btn_finish.textContent = improved_mix.btn_end
    btn_add_temperature.textContent = improved_mix.btn_label_add
    btn_add_humidity.textContent = improved_mix.btn_label_add
    btn_add_viscosity.textContent = improved_mix.btn_label_add
    btn_ready.textContent = improved_mix.btn_modal_start_fill
    btn_print.textContent = improved_mix.btn_print
    btn_close_1.forEach(item => {
        item.textContent = improved_mix.btn_close
    })
    btn_graph_subs.textContent = improved_mix.btn_ready_sustance
    btn_graph_combi.textContent = improved_mix.btn_shake

    btn_accept. forEach(item => {
        item.textContent = improved_mix.acept_btn
    })
    btn_edit. forEach(item => {
        item.textContent = improved_mix.edit_btn
    })

}