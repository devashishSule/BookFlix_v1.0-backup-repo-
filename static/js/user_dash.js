$(document).ready(function() {
    $('#data_input').click(function(e) {
        console.log($('#course').val())
        console.log($('#year').val())
        $.ajax({
                data: {
                    'Course': $('#course').val(),
                    'Year': $('#year').val(),
                    'Semester': $('#sem').val()
                },
                type: 'POST',
                url: '/user_dashboard'
            })
            .done(function(data) {
                if (data.answer) {
                    console.log(data.answer)
                    $('#subjects').text(data.answer).show()
                    if ($('#sem').val() == 'odd' && $('#year').val() == 'SY') {
                        $('#python').show();

                    } else {
                        $('#python').hide();
                    }
                }


            })
    })

})