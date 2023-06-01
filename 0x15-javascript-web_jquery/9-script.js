<head>
	<script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
$(function() {
  const url = "https://fourtonfish.com/hellosalut/?lang=fr";

  $.get(url, function(response) {
    const hello = response.hello;
    const $div = $("<div id='hello'></div>").text(hello);
    $("body").append($div);
  });
});

