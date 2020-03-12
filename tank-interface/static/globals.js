$(document).ready(function() {
    $('#up-btn').on('click', {dir: "up"}, sendDirection);
    $('#down-btn').on('click', {dir: "down"}, sendDirection);
});

function sendDirection(event) {
    var direction = event.data.dir
    var send = {
        payload: direction
    };
    console.log(send);
    $.ajax({
        type:'POST',
        data:JSON.stringify(send),
        url:'/orders',
        dataType:'JSON'
    }).done(function(response) {
        console.log(response.data.direction);
        $('#current-pos').text(response.data.direction);
    });
}
