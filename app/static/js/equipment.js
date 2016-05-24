var main = function(){
	
	$(".sublevel").load("/passivnieComponentiVols");
	

	$(".show_email:checkbox").on('change', function(){
		$('.email').toggleClass('hidden');
	});
	$(".show_comment:checkbox").on('change', function(){
		$('.comment').toggleClass('hidden');
	});
	$(".levels li").on('click',function(){
		var href = $('a',this).attr('href');
		$(".levels li.active").toggleClass("active");
		$(this).toggleClass("active");
		$(".sublevel").load(href);
		return false;
	});
	
}

$(document).ready(main);

