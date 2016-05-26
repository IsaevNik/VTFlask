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
		
		if (input_val > 1){
			$(this).prev().val(input_val-1);
		} else {
			$(this).prev().val(1);
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
 		var item_count = $("input", input_form).val(); //получаем колличество

 		var description = $(this).parents('.counter').prev();
 		var item_name = $("p",description).text(); //получаем название выбранного товара

 		var price_block = $(this).parents('.counter').prev(); 
 		var item_coast = $(".item-coast p",this).text();
 		
 		total_coast_of_item = +count * (+item_coast);
 		alert(total_coast_of_item);

 		var newItem = $('<li class="list-group-item"></li')
        .append('<span class="glyphicon glyphicon-remove-circle remove-item"></span>')
        .append($('<span/>',{
        	"class" : "count",
        	text : item_count + " шт."
        }))
        .append($('<span/>',{
        	"class" : "name-item",
        	text : item_name
        }));
		
 		if (count != 0){
 			$('.client-cart').prepend(newItem);
 		}
 	});
}

$(document).ready(main);

