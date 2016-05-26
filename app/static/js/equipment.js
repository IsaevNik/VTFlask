var main = function(){
	
	$(".sublevel").load("/passivnieComponentiVols");
	var telephon_pattern = /^(\+?\d{1}\(?\d{3}\)?\d{3}-?\d{2}-?\d{2})$/;
 	var name_pattern = /^([а-яА-Я ]+)$/;
 	var mail_pattern = /^[\w-\.]+@[\w-]+\.[a-z]{2,3}$/;
 	var sum = 0.0;

	$(".show_email:checkbox").on('change', function(){
		$('.email').slideToggle('slow');
	});
	$(".show_comment:checkbox").on('change', function(){
		$('.comment').slideToggle('slow');
	});
	$(".levels li").on('click',function(){
		var href = $('a',this).attr('href');
		$(".levels li.active").toggleClass("active");
		$(this).toggleClass("active");
		$(".sublevel").load(href);
		return false;
	});
	
	$('.user-form input').on('focus',function(){
 		$(this).next().removeClass("glyphicon-ok");
 		$(this).next().removeClass("glyphicon-remove");
 		$(this).parent().removeClass("has-success");
 		$(this).parent().removeClass("has-error");
 	
 	});
 	$('#client_name').blur(function(){  //Валидация имени
 		var name = $(this).val();
 		if (name.match(name_pattern) != null){
 			$(this).parent().addClass("has-success");
 			$(this).next().addClass("glyphicon-ok");
 		} else {
 			$(this).parent().addClass("has-error");
 			$(this).next().addClass("glyphicon-remove");
 		}
 	});
 	
 	$('#client_telephone').blur(function(){ //Валидация телефона
 		var telephon = $( this ).val();
 		if ( telephon.match( telephon_pattern ) != null ){
 			$( this ).parent().addClass("has-success");
 			$( this ).next().addClass("glyphicon-ok");
 		} else {
 			$( this ).parent().addClass( "has-error" );
 			$( this ).next().addClass( "glyphicon-remove" );
 		}
 	});
 	$('#client_email').blur(function(){ //Валидация адреса электронной почты
 		var mail = $(this).val();
 		if ( mail.match( mail_pattern ) != null ){
 			$(this).parent().addClass("has-success");
 			$(this).next().addClass("glyphicon-ok");
 		} else {
 			$(this).parent().addClass("has-error");
 			$(this).next().addClass("glyphicon-remove");
 		}
 	});
 	
 	$('.user-form').focusin(function(){ 
 		$(this).toggleClass("focus-form");
 	});
 	$('.user-form').focusout(function(){
 		$(this).toggleClass("focus-form");
 	});

 	$('.client-cart').on('click','.remove-item',function(){ //Удаление строки из корзины 
 		var sum_in_user_cart = parseFloat($('.total-count').text());
 		var item_count = parseInt($(this).next().text().split('x')[0]);
 		var item_coast = parseFloat($(this).next().text().split('x')[1]);

 		var total_coast_of_item = item_count * item_coast;
 		sum_in_user_cart = sum_in_user_cart - total_coast_of_item;

 		if ((sum_in_user_cart ^ 0) === sum_in_user_cart){
 				sum_in_user_cart = sum_in_user_cart + ".00 руб.";
 			} else {
 				sum_in_user_cart = parseFloat(sum_in_user_cart.toFixed(2))
 				sum_in_user_cart = sum_in_user_cart + " руб.";
 			}
 		$('.total-count').text(sum_in_user_cart);
 		$(this).parent('.list-group-item').remove();
 	});
}

$(document).ready(main);

