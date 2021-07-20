// var btn = document.getElementById(Search)

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var xhr = new XMLHttpRequest();

var ourRequest = new XMLHttpRequest();
ourRequest.open("GET", "http://127.0.0.1:5000/api");
ourRequest.onload= function(){
	var ourData = JSON.parse(ourRequest.responseText);
	var name = ourData[1].name;
	console.log(ourData[1]);
	console.log(name)
}
ourRequest.send()

var title ="java at tinapay"
console.log(title);