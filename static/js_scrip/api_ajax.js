$(document).ready(function() {
    // get or read with arg
    $('#barcode_read').on('click', function() {
        // console.log("set 2 ok");
        // console.log($('#barcode_id').val())
        let query_key = "barcode_id";
        let query_value = $('#barcode_id').val();
        let url_ko = `http://127.0.0.1:5000/api_barcode/${query_key}/${query_value}`;
        //       console.log(url_ko)
        // console.log(`http://127.0.0.1:5000/api_barcode/${query_key}/${query_value}`);
        $.ajax({
            data: {
                barcode_id: $('#barcode_id').val(),
            },
            type: 'GET',
            url: url_ko
        }).done(function(data) {
            console.log(data.barcode_id);
            console.log(data.id);
            console.log(data.barcode_id);
            console.log(data.item_name);
            console.log(data.part_no);
            console.log(data.serila_no);
            console.log(data.description);
            console.log(data.remarks);
            console.log(data.prod_pic);
            console.log(data.mimetype_db);
            console.log(data.date_added);
            console.log(data.user_id)

            $("#item_name").val(data.item_name);
            $("#brand_name").val(data.brand_name);
            $("#part_no").val(data.part_no);
            $("#serila_no").val(data.serila_no);
            $("#description").val(data.description);
            $("#remarks").val(data.remarks);
            $("#prod_pic").val(data.prod_pic);

        });

        //         event.preventDefault();

    });







});