$(document).ready(function() {
    $('#go').on('submit', function(e) {
        $('#loading').show();
        $.ajax({
                data: {
                    'question': $('#question').val()
                },
                type: 'POST',
                url: '/user_dashboard/chatbot'
            })
            .done(function(data) {

                if (data.answer) {
                    $('#loading').hide()
                    console.log(data.answer)
                        // answer = ({ message: (data.answer.choices[0].text) })
                        // console.log(answer)
                    $('#answer').text(data.answer.choices[0].text).show()

                }
            })

        e.preventDefault();
    })
})