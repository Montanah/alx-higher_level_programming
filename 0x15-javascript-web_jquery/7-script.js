<head>
     <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
$.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (result) {
	$("#character").text(result.name);
});
