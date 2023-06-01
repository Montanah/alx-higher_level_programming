<head>
     <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function (result) {
	for (let element of result.results) {
    const item = $('<li></li>').text(element.title);
    $('#list_movies').append(item);
  }
});
