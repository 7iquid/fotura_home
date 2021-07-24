$(document).ready(function() {
    // get or read with arg
    $('#barcode_read').on('click', function() {

        let url_ko = 'http://127.0.0.1:5000/api_barcode/tamina';
        data_2 = $("#barcode_id").serializeJSON();
        console.log(data_2)
        const settings = {
                url: url_ko,
                // dataType:"headers",
                 data :data_2,
                method: "GET",
                
            };
    $.ajax(settings).done(function (response) {
        console.log(response);
        
        });

    });
    $('#barcode_create').on('click', function() {

        let url_ko = 'http://127.0.0.1:5000/api_barcode/tamina';
        data_2 = $('form').serializeJSON();
        const settings = {
                url: url_ko,
                dataType:"json",
                 data : JSON.stringify(data_2),
                method: "PUT",
                headers: {
                    "x-api-key": "API_KEY",
                    "Content-type": "application/json"
                }
                
            };
    $.ajax(settings).done(function (response) {
        console.log(response);
        });

    });



});