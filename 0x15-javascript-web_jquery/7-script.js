// a JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
// and displays it in the HTML tag DIV#character.

$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', 
    function (data) {
    $('#character').text(data.name);
  });
});