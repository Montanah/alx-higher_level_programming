 <head>
      <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
      <script type="text/javascript" src="102-script.js" defer></script>
 </head>
 $(document).ready(function () {
	$("#btn_translate").click( function () {
		const languageCode = ("#language_code").val();
		const apiUrl = "https://www.fourtonfish.com/hellosalut/hello/" + languageCode;

	 $.get(apiUrl).done(function(response) {
        const translation = response.hello;
        $("#hello").text(translation);
          });
	});
 });
