$('document').ready(function () {
	// Attach a click event handler to the <div> with ID "add_item"
	$('DIV#add_item').click(function () {
		$('UL.my_list').append('<li>Item</li>');
	});
	$('DIV#remove_item').click(function () {
		$('UL.my_list li:last').remove();
	});
	$('DIV#clear_list').click(function () {
		$('UL.my_list').empty();
	});
});
