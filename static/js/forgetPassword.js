$(document).ready(function() {
    $('#recovery').on('submit', function(e) {
        $.ajax({
                data: {
                    'email': $('#email').val()
                },
                type: 'POST',
                url: '/forgetPassword'
            })
            .done(function(data) {
                if (TypeError()) {
                    console.error('Lavdyaa barobar taak')
                    $('#errorBox').show();
                }
            })

        e.preventDefault();
    })
})