$(document).ready(function() {
    // get or read with arg
    $('#barcode_read').on('click', function() {

        let url_ko = 'http://127.0.0.1:5000/api_barcode/tamina';
        data_2 = $("#barcode_id").serializeJSON();
        console.log(data_2)
        const settings = {
            "url": url_ko,
            "data": { "cake": data_2.barcode_id },
            "method": "GET",
            error: function(xhr, ajaxOptions, thrownError) {
                if (xhr.status == 404) {
                    alert(thrownError);
                }
            },
        };

        $.ajax(settings).done(function(response) {
            console.log(response);
            $("#item_name").val(response.item_name);

            // alert("good");
            // Object.entries(response).forEach(([k, v], i) => console.log(i, k, v))

            Object.entries(response).forEach(([k, v], i) => $("#" + k).val(v));
            // let value = v;


            // console.log(i, k, v))


            // console.log(response.item_name);
        });
    });

    $('#barcode_create').on('click', function() {

        let url_ko = 'http://127.0.0.1:5000/api_barcode/tamina';
        data_2 = $('form').serializeJSON();
        const settings = {
            url: url_ko,
            dataType: "json",
            data: JSON.stringify(data_2),
            method: "PUT",
            headers: {
                "x-api-key": "API_KEY",
                "Content-type": "application/json"
            }

        };
        $.ajax(settings).done(function(response) {
            console.log(response);

        });

    });



});