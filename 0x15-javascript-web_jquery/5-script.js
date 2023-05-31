<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
$(function () {
	$(#add_item).click(function () {
		const item = $("<li></li>").text("item");
		$(UL.my_list).append(item);
	});
});
