
function update_level_from_signal(e){
    console.log("key: " + e.key + " --- > code: " + e.code)
    if(e.key == "+"){
      level+=5;
      if(level > 120)
        level = 120;
    draw_fill_levels();
    }else if(e.key == "-"){
        level-=5;
        if(level < 0)
          level = 0;
      draw_fill_levels();
    }
    update_level_in_interval(e);
    update_level_outside_interval(e);
    update_level_ok();
    update_gr();
    console.log('level: '+ level + '   level_ok: '+ level_ok + '   level_in_interval: '+ level_in_interval + '     level_outside_interval: ' + level_outside_interval );
    console.log('level: '+ level + '   gr_level_ok: '+ gr_level_ok + '   gr_level_in_interval: '+ gr_level_in_interval + '     gr_level_outside_interval: ' + gr_level_outside_interval );
  }
  
  function update_level_ok(){
    if(level <= 90)
      level_ok = level;
    else 
      level_ok = 90;
  }
  
  function update_level_in_interval(e){
    if((level > 90) && (level < 110)){
      if(e.key == '+'){
        level_in_interval +=2;
        if(level_in_interval > 20){
          level_in_interval = 20;
        }
      }else if(e.key == '-'){
        level_in_interval -=2;
        if(level_in_interval < 0){
          level_in_interval = 0;
        }
      }
    }else if(level <= 90){
      level_in_interval = 0;
    }else{
      level_in_interval = 20;
    }
  }
  
  function update_level_outside_interval(e){
    if(level >= 110){
      if(e.key == '+'){
        level_outside_interval +=2;
        if(level_outside_interval > 20){
          level_outside_interval = 20;
        }
      }else if(e.key == '-'){
        level_outside_interval -=2;
        if(level_outside_interval < 0){
          level_outside_interval = 0;
        }
      }
    }else{
      level_outside_interval = 0;
    }
  }
  
  function update_gr(){
    gr_level_ok = weight_containe*level_ok/100;
    gr_level_in_interval = weight_containe*level_in_interval/100;
    gr_level_outside_interval = weight_containe*level_outside_interval/100;
  }
  
  
  function draw_fill_levels_stacked_bar(){
    new Chart(document.getElementById("fillLeves"), {
    type: 'bar',
    data: {
        labels: ['Nivel'],
        datasets: [
        {
            label: "POR DEBAJO",
            backgroundColor: ["#F2D300"],
            //data: [level_ok],
            data: [gr_level_ok],
        }, 
        {
          label: "OK",
          backgroundColor: ["#00aa00"],
          //data: [level_in_interval],
          data: [gr_level_in_interval],
        },
        {
          label: "POR ENCIMA",
          backgroundColor: ["#aa0000"],
          //data: [level_outside_interval],
          data: [gr_level_outside_interval],
        }
        ]
    },
    options: {
        animation: {
          duration: 0 // general animation time
      },
      hover: {
          animationDuration: 0 // duration of animations when hovering an item
      },
      responsiveAnimationDuration: 0 // animation duration after a resize
  ,
  events: [],
        legend: { display: true },
        tooltips: {
          enabled: false,
        },
        title: {
        display: true,
        text: 'Nivel de pintura ' + level + '%',
            maintainAspectRatio: false,
            responsive: true,
        },
        scales: {
          xAxes: [{
            stacked: true,
          }],
        yAxes: [{
            display: true,
            stacked: true,
            ticks: {
                min: 0, 
                max: parseInt(max_weight_container) //135 // (%)
            },
            scaleLabel:{
              display: true,
              labelString: 'gramos'
            }
        }]
    }
    }
    });
  }

////// Funciones de prueba .... se pueden borrar en el producto final ... 
function draw_fill_levels(){
    new Chart(document.getElementById("fillLeves"), {
    type: 'bar',
    data: {
        labels: ['Nivel'],
        datasets: [
        {
            label: "Nivel de pintura",
            backgroundColor: ["#00aa00"], //, "#aa0000"],
            //data: data__ 
            data: [level], //, 6]
        }
        ]
    },
    options: {
        animation: {
          duration: 0 // general animation time
      },
      hover: {
          animationDuration: 0 // duration of animations when hovering an item
      },
      responsiveAnimationDuration: 0 // animation duration after a resize
  ,
  events: [],
        legend: { display: false },
        tooltips: {
          enabled: false,
        },
        title: {
        display: true,
        text: 'Nivel de pintura',
            maintainAspectRatio: false,
            responsive: true,
        },
        scales: {
        yAxes: [{
            display: true,
            stacked: false,
            ticks: {
                min: 0, // minimum value
                max: 120 // maximum value
            }
        }]
    }
    }
    });
  }