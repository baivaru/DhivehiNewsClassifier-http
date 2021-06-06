$(document).ready(function() {
    $('#generate-button').click(function(e){
        e.preventDefault();
        var news = $("#news").val();

        $('#results').html("");

        axios.get(`/api/classify/${news}`).then(function (response) {
            var raw = response.data.raw;

            $('#results').append(`<p>${raw}</p>`);
        });
    });
})