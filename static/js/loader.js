$(document).ready(function(){
	$(".content").load("/main_page");
    $(".content").attr("id", "main_page");
	$(".carousel").carousel({
		interval: 4000
	});
	$(".carousel").carousel('cycle');
});

$(".navbar-nav > li").click(function(){
	
    var current_page = $(".navbar-nav > li.active")
	$(current_page).toggleClass("active");
	
    var page = $("a",this).attr("href");
    var content_id = page.substr(1);

    $('.content').attr("id", content_id);
    $(".content").load(page);

	$(this).toggleClass('active');
	
	if ($(".collapse").hasClass("in")) {
		$(".collapse").collapse("hide");
	}
	return false;
});


