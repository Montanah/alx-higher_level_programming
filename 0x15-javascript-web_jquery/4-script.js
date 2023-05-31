<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
$(function () {
	$("#toggle_header").click(function () {
		$(".red, .green").toggleClass("red green");
	});
});
