/*
avaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

The translation of “hello” must be displayed in the HTML tag DIV#hello
*/

$(document).ready(function (){
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});