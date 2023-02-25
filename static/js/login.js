function show() {
    var x = $("#password");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
                data: {

                    'username': $('#username').val(),
                    'password': $('#password').val()

                },
                type: 'POST',
                url: '/login'
            })
            .done(function(data) {
                console.log(data)
                if (data.error) {
                    $('#error').show()
                        // $('#success').text(data.message).hide()
                } else {
                    window.location.replace(data.status)
                }
            })

        event.preventDefault();
    })
})