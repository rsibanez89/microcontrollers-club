$(document).ready(function() {
    $('#up-btn').on('click', goForward);
    $('#down-btn').on('click', goStop);
});

function goForward(event) {
    $.ajax({
        type:'GET',
        url:'/forward',
        dataType:'JSON'
    }).done(function(response) {
        console.log(response.data.data.horz);
        $('#current-pos').text(response.data.data.horz);
    });
}
function goStop(event) {
    $.ajax({
        type:'GET',
        url:'/stop',
        dataType:'JSON'
    }).done(function(response) {
        console.log(response.data.data.horz);
        $('#current-pos').text(response.data.data.horz);
    });
}
