var main = function(){
	
}


$(document).ready(main);

$('#show').on('click', function(){
	$('.alert').toggleClass('hidden');
});

$(":checkbox").on('change', function(){
	$('.email').toggleClass('hidden');
});

$('.panel-heading').on('click',function(){
	var parent = $(this).parents('.panel');
	$('#collapseOne',parent).collapse('toggle');
	$('.panel-title a',this).toggleClass('active');
});