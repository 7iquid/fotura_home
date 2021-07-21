
var barcode_create = document.getElementById("barcode_create")
var barcode_read = document.getElementById("barcode_read")
var barcode_update = document.getElementById("barcode_update")
var barcode_delete = document.getElementById("barcode_delete")


var Barcode_Data = new XMLHttpRequest();


Barcode_Data.open("GET", "http://127.0.0.1:5000/api");
Barcode_Data.onload= function(){
	var ourData = JSON.parse(ourRequest.responseText);
	var name = ourData[1].name;
	console.log(ourData[1]);
	console.log(name)
}
ourRequest.send()

var title ="java at tinapay"
console.log(title);