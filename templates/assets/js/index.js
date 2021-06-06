$(document).ready(function() {
    $('#generate-button').click(function(e){
        e.preventDefault();
        var raw_news = $("#news").val();

        $('#results').html("");

        axios.post(`/api/classify/`, {news : raw_news}).then(function (response) {
            var result = response.data.category;
            $('#results').append(`${result}`);
        });
    });
})