var main = function(){
	
	$(".sublevel").load("passivnieComponentiVols.html");
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
	$('#client_name').blur(function(){
		var name = $(this).val();
		if (name.match(name_pattern) != null){
			$(this).parent().addClass("has-success");
			$(this).next().addClass("glyphicon-ok");
		} else {
			$(this).parent().addClass("has-error");
			$(this).next().addClass("glyphicon-remove");
		}
	});
	
	$('#client_telephone').blur(function(){
		var telephon = $(this).val();
		if (telephon.match(telephon_pattern)!=null){
			$(this).parent().addClass("has-success");
			$(this).next().addClass("glyphicon-ok");
		} else {
			$(this).parent().addClass("has-error");
			$(this).next().addClass("glyphicon-remove");
		}
	});
	$('#client_email').blur(function(){
		var mail = $(this).val();
		if (mail.match(mail_pattern)!=null){
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
}

$(document).ready(main);

