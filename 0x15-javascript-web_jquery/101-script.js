<head>
      <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	  <script type="text/javascript" src="101-script.js" defer></script>
 </head>
 $(document).ready(function () {
	$("#add_item").click(function() {
        $("ul.my_list").append("<li>Item</li>");
      });

      $("#remove_item").click(function() {
        $("ul.my_list li:last-child").remove();
      });

      $("#clear_list").click(function() {
        $("ul.my_list").empty();
      });
 });
