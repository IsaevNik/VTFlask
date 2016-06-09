var main = function(){
	
	$(".sublevel").load("/level1");
	var telephon_pattern = /^(\+?\d{1}\(?\d{3}\)?\d{3}-?\d{2}-?\d{2})$/;
 	var name_pattern = /^([а-яА-Я ]+)$/;
 	var mail_pattern = /^[\w-\.]+@[\w-]+\.[a-z]{2,3}$/;
 	var sum = 0.0;



 	var successMessage = $('<div class="alert alert-success"></div>')
        .append('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>')
        .append('<strong>Отлично! </strong>Наш менеджер свяжется с вами для уточнения деталей.');

    function errorMessage(text_str, text_sm){
    	var errorElement = $('<div class="alert alert-danger"></div>')
        .append('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>')
        .append('<strong>'+text_str+'</strong>'+text_sm);

        return errorElement;
    }
    
    var warningMessage = $('<div class="alert alert-warning"></div>')
        .append('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>')
        .append('<strong>Заявка пуста! </strong> Вы не добавили ни одного товара в корзину.');

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

 	function is_valid(input_block){
 		if ($(input_block).next().hasClass("glyphicon-ok")) {
 			return true;
 		} else {
 			return false;
 		}
 	};


 	function reset_form() {
 		$('.sublevel').load('/passivnieComponentiVols');
 		if($(".show_email").is(':checked')) {
 			$('.email').slideToggle('fast');
 		}
 		if($(".show_comment").is(':checked')) {
 			$('.comment').slideToggle('fast');
 		}
 		$('.levels li.active').removeClass('active');
 		$('.levels li:first-child').addClass('active');
 		$('.item-of-cart').remove();
 		$('.total-count').text("0.00 руб.");
 		$('#form')[0].reset();
 		$('.user-form input').each(function(){
 			$(this).next().removeClass("glyphicon-ok");
 			$(this).parent().removeClass("has-success");
 		});
 		

 	};

 	function request_hendler(name_input, telephon_input, email_input, comment_input) {
 		var data_of_request = {}


 		data_of_request['client_name'] = $(name_input).val();
 		data_of_request['client_telephon'] = $(telephon_input).val();
 		data_of_request['client_email'] = $(email_input).val();
 		data_of_request['client_comment'] = $(comment_input).val();
 		data_of_request['items'] = new Array();

 		$('.item-of-cart').each(function(){
 			var item_for_send = {};
 			item_for_send['name_of_item'] = $(this).children('.name-item').text();
 			item_for_send['count'] = parseInt($(this).children('.count').text().split('x')[0]);
 			data_of_request['items'].push(item_for_send);
 		});
 		
 		

 		$.ajax({
 			url: '/equipments',
 			type: 'POST',
 			contentType: "application/json; charset=utf-8",			
 			data: JSON.stringify(data_of_request),
 			
 			success: function(response) {
 				$('.client-cart').after(successMessage);
 				reset_form();
 			},
 			error: function(error) {
 				$('.client-cart').after(errorMessage("Ошибка на сервере!","Мы не можем обработать ваш запрос"));
 			}
 		});
 		
 	};

 	$('.search span').on('click', function(){
 		var userSearchRequest = {};

 		var textOfRequest = $(this).next().val();
 		if (textOfRequest != ''){
 			$(".levels li.active").toggleClass("active");
 			userSearchRequest['text'] = textOfRequest;
 			$.ajax({
	 			url: '/search',
	 			type: 'POST',
	 			contentType: "application/json; charset=utf-8",			
	 			data: JSON.stringify(userSearchRequest),
 				dataType: "html",
	 			success: function(response) {
	 				$(".sublevel").html(response);
	 				$('.collapse').toggle();
	 			},
	 			error: function(error) {
	 				$('.sublevel').append(errorMessage("Ошибка на сервере!","Мы не можем обработать ваш запрос"));
	 			}
 			});
 		}
 	});

 	$('.submit-button').on('click',function(){
 		
 		$('.alert').remove();

 		var telephon_input = $("#client_telephone");
 		var name_input = $("#client_name");
 		var email_input = $("#client_email");
 		
 		if ($('.client-cart').children().length == 1){ //если карзина пуста предупреждение
 			$('.client-cart').after(warningMessage);
 			return false;
 		}
 		if($(".show_email").prop("checked")) { 
 			if (is_valid(telephon_input) && is_valid(name_input) && is_valid(email_input)){ //валидация формы с почтой
 				;
 			} else {
 				$('.client-cart').after(errorMessage("Ошибка!","Проверьте корректность данных"));
 				return false;
 			}
 		} else {
 			if (is_valid(telephon_input) && is_valid(name_input)) { //валидация формы без почты
 				;
 			} else {
 				$('.client-cart').after(errorMessage("Ошибка!","Проверьте корректность данных"));
 				return false;
 			}
 		}

 		request_hendler(name_input, telephon_input, email_input, 'textarea');
 		
 		
 	});
}

$(document).ready(main);

