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
	
}

$(document).ready(main);

