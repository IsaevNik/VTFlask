var main = function(){
	$(".history_short .more").click(function(){    
		$(this).toggle();
		$(".history_long").slideToggle(400);
	});
	$(".history_long span").click(function(){
		$(".history_long").slideToggle(100);
		$(".history_short .more").toggle();
	});
	$(".staff_short .more").click(function(){
		$(this).toggle();
		$(".staff_long").slideToggle(400);
	});
	$(".staff_long span").click(function(){
		$(".staff_long").slideToggle(100);
		$(".staff_short .more").toggle();
	});
	$(".activity_short .more").click(function(){
		$(this).toggle();
		$(".activity_long").slideToggle(400);
	});
	$(".activity_long span").click(function(){
		$(".activity_long").slideToggle(100);
		$(".activity_short .more").toggle();
	});
};

$(document).ready(main);
