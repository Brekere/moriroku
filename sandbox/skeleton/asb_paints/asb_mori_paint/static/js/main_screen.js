document.getElementById('fill_pro').focus()
var listW = []

fetch('static/config_json/workers.json').then(response => {
  return response = response.json()
}) .then(data => {
  console.log(data[0]['list'].length)
  listW = data[0]['list']
})

function example(lang){
  location.hash = lang
  location.reload();
}

var language = {
    en: {
        title: "Painting Mixing Control System",
        mix: "Filling/Mixing Process",
        viscosity: "Viscosity Process"
    },
    sp:{
        title: "Sistema de Control de Mezclado de Pinturas",
        mix: "Proceso de LLenado/Mezclado",
        viscosity: "Proceso de Viscosidad"
    }
}

function languageSelect(lang){
  fetch('static/config_json/language.json').then(response => {
    return response = response.json()
  }) .then(data => {
    console.log(data[0])
  })
}

if(window.location.hash){
    if(window.location.hash == "#en"){
        title_sys.textContent =language.en.title
        fill_pro.textContent = language.en.mix
        visc_pro.textContent = language.en.viscosity
    } else if( window.location.hash == "#sp"){
        title_sys.textContent = language.sp.title
        fill_pro.textContent = language.sp.mix
        visc_pro.textContent = language.sp.viscosity
    }
}

window.addEventListener("keydown", function(e) {
  var btn = document.getElementById('fill_pro')

  switch(e.key){
      case('PageDown'):
        this.document.getElementById('fill_pro').focus()
        break;
      case('PageUp'): 
        break;
  }

  if(e.key == 'b'){
    document.getElementById("fill_pro").click();
  }
})

$('#infoModal').on('shown.bs.modal', function () {
  const time = 6000
  setTimeout(function(){
      $('#infoModal').modal('hide')
      $('#CredentialsModal').modal('show')
  }, time)
});

$('#CredentialsModal').on('show.bs.modal', () => {
  const timer = 4000
  setTimeout(() => {
    $('#CredentialsModal').modal('hide')
    window.location.replace('http://127.0.0.1:5000/OT_Detail')
  }, timer);
})