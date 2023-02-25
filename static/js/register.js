console.log("HelloWorld")

function show1() {
    var x = $("#pass1");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

function show2() {
    var x = $("#pass2");
    if (x.attr('type') === "password") {
        x.attr('type', 'text')
    } else {
        x.attr('type', 'password')
    }
}

// function show1() {
//     var x = $("#pass1");
//     if (x.attr('type') === "password") {
//         x.attr('type', 'text')
//     } else {
//         x.attr('type', 'password')
//     }
// }


// function verify() {
//     var a = $("#pass1").val();
//     var b = $("#pass2").val();
//     if ((a == b) && a != null && b != null) {
//         return alert('Registeration Successful...');
//     } else {
//         return alert('Password entered does not match or empty. Please fill out again')
//     }
// }

$(document).ready(function() {
    $('#form').on('submit', function(e) {
        $.ajax({
                data: {
                    'firstName': $('#content1').val(),
                    'lastName': $('#content2').val(),
                    'username': $('#username').val(),
                    'email': $('#email').val(),
                    'password1': $('#pass1').val(),
                    'password2': $('#pass2').val(),
                },
                type: 'POST',
                url: '/register'
            })
            .done(function(data) {
                console.log(data)
                if (data.error) {
                    $('#error').show()
                    $('#alert-1').hide()
                } else {
                    $('#alert-1').show()
                    $('#error').hide()
                }
            })

        e.preventDefault();
    })
})