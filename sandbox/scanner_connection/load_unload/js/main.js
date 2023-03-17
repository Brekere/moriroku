var currentPage = "";

$(document).ready(function () {
    $('#load1').click(function () {
        loadSource('page1', 'body');
    });
    $('#load2').click(function () {
        loadSource('page2', 'body');
    });
});

function loadSource( page, element){
    currentPage = page;
    $('#container').load('views/' + page + '.html', element);
    $.getScript('js/' + page + '.js');
    $('#css').prop('disabled', true).remove();
    $('head').append('<link rel="stylesheet" href="css/' + page + '.css" type="text/css" />');
}