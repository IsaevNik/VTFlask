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
        var sum_in_user_cart = parseFloat($('.total-count').text());
     
 		var input_form = $(this).parent().prev();
 		var item_count = $("input", input_form).val(); //получаем колличество

 		var description = $(this).parents('.counter').prev();
 		var item_name = $("p",description).text(); //получаем название выбранного товара

 		var price_block = $(this).parents('.counter').next(); 
 		$(".item-coast p b",this).css({"background-color":"red"});

 		var item_coast = $(price_block).find('p').text();
 		
 		var total_coast_of_item = Number(item_count) * Number(item_coast);

 		var newItem = $('<li class="list-group-item item-of-cart"></li>')
        .append('<span class="glyphicon glyphicon-remove-circle remove-item"></span>')
        .append($('<span/>',{
        	"class" : "count",
        	text : item_count + " шт. x " + item_coast
        }))
        .append($('<span/>',{
        	"class" : "name-item",
        	text : item_name
        }));
		
 		if (item_count != 0){
 			sum_in_user_cart = sum_in_user_cart + total_coast_of_item;
 			if ((sum_in_user_cart ^ 0) === sum_in_user_cart){
 				sum_in_user_cart = sum_in_user_cart + ".00 руб.";
 			} else {
 				sum_in_user_cart = parseFloat(sum_in_user_cart.toFixed(2));
 				sum_in_user_cart = sum_in_user_cart + " руб.";
 			}
 			$('.client-cart').prepend(newItem);
 			$('.total-count').text(sum_in_user_cart);
 		}
 	});
}

$(document).ready(main);

