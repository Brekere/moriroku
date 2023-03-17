var color_level = "#F2D300"

function update_level_from_data(weight){
  gr_level = weight;
  level = 100*gr_level/max_weight_mix;
  //
  gr_level_in_interval = 0;
  level_in_interval = 0;
  gr_level_outside_interval = 0;
  level_outside_interval = 0;
  if(gr_level < gr_min_accept){
    color_level = "#F2D300"
    level_low = level;
    gr_level_low = gr_level;
  } else{
    level_low = 90;
    gr_level_low = max_weight_mix*0.9;
    if( gr_level >= gr_min_accept && gr_level < gr_max_accept ){
      color_level = "#00aa00"
      gr_level_in_interval = gr_level - gr_min_accept;
      level_in_interval = 100*gr_level_in_interval/max_weight_mix;
    }else{
      color_level = "#aa0000"
      gr_level_in_interval = max_weight_mix*0.20;
      level_in_interval = 20;
      gr_level_outside_interval = 100*(gr_level - gr_max_accept)/max_weight_mix;
      level_outside_interval = 100*gr_level_outside_interval/max_weight_mix;
    }
  } 
  //console.log('level: '+ level + '   level_low: '+ level_low + '   level_in_interval: '+ level_in_interval + '     level_outside_interval: ' + level_outside_interval );
  //console.log('gr_level: '+ gr_level + '   gr_level_low: '+ gr_level_low + '   gr_level_in_interval: '+ gr_level_in_interval + '     gr_level_outside_interval: ' + gr_level_outside_interval );
}
  
  function draw_fill_levels_stacked_bar(id){
    new Chart(document.getElementById(id), {
    type: 'bar',
    data: {
        indexLabelFontSize: 30,
        labels: ['Nivel'],
        datasets: [
        {
            label: "Nivel",
            backgroundColor: [color_level],
            data: [gr_level],
            //data: [gr_level_low],

        },
      /* ],
      dataPoints: [
        {
          x: 0.5,
          y: level_outside_interval / 2,
          indexLabel: `${level.toFixed(2)} + '%'`,
          indexLabelPlacement: "inside", 
          indexLabelFontColor: "grey"
        } *//* , 
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
        } */
        ]
    },
    options: {
        animation: {
          duration: 0 // general animation time
      },
      hover: {
          animationDuration: 0 // duration of animations when hovering an item
      },
      responsiveAnimationDuration: 0, // animation duration after a resize
      maintainAspectRatio : false
    , 
  events: [],
        legend: { display: true },
        tooltips: {
          enabled: false,
        },
        title: {
        display: true,
        text: 'Nivel de pintura ' + level.toFixed(2) + '%',
            fontSize: 50,
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
                max: parseInt(max_weight_mix_accept), //135 // (%)
                fontSize: 30
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