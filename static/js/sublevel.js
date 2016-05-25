var main = function(){

	$('.panel-heading').on('click',function(){
		var parent = $(this).parent('.panel');
		$('.collapse',parent).collapse('toggle');
		$('.panel-title a',this).toggleClass('active');
	});
	$( ".input-group-addon" ).on('mousedown',function() {
		$(this).addClass( "click" );
	});
	$( ".input-group-addon" ).on('mouseup',function() {
		$( this ).removeClass( "click" );
	});
	$(".input-group-addon.up").on('click', function(){
		var input_val = +($(this).next().val());
		$(this).next().val(input_val+1);
		
	});
	$(".input-group-addon.down").on('click', function(){
		var input_val = +($(this).prev().val());
		
		if (input_val > 0){
			$(this).prev().val(input_val-1);
		} else {
			$(this).prev().val(0);
		};
		
	});
	$( ".shoping-cart" ).on('mousedown',function() {
		$(this).addClass( "click" );
	});
	$( ".shoping-cart" ).on('mouseup',function() {
		$( this ).removeClass( "click" );
	});
	$(".shoping-cart").on('click', function(){
		var input_form = $(this).parent().prev();
		var description = $(this).parents('.counter').prev();
		var item_name = $("p",description).text();
		var count = $("input", input_form).val();
		var line = item_name + " кол-во." + count;
		//alert(line);
		if (count != 0){
			$("<li>", {
				"class": "clickme",
				text: line,
				}).appendTo(".client-cart");
		}
	});
	
}

$(document).ready(main);

