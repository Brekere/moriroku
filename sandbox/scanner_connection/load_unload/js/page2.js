$(document).ajaxComplete(function () {
    if(currentPage == 'page2'){
        $('#test1').click(function () {
            console.log('page2');
        });
        /*$('#test2').click(function () {
            console.log('page2');
        });*/
    }
});