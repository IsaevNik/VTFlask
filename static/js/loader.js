$(document).ready(function(){
	$(".content").load("main.html");
    $(".content").attr("id", "main");
	$(".owl-carousel").owlCarousel({
		navigation : false, // показывать кнопки next и prev 
		autoPlay: 3000,
		slideSpeed : 8000,
		paginationSpeed : 4000,

	 
		items : 1, 
		itemsDesktop : false,
		itemsDesktopSmall : false,
		itemsTablet: false,
		itemsMobile : false
	});
	/*var owl = $(".owl-carousel").data('owlCarousel');
	owl.destroyControlls();*/
});

$(".navbar-nav > li").click(function(){
	
    var current_page = $(".navbar-nav > li.active")
	$(current_page).toggleClass("active");
	
    var page = $("a",this).attr("href");
    var content_id = page.split('.')[0];
	
    $(".content").attr("id", content_id);
    $(".content").load(page);
	$(this).toggleClass("active");
	
	if ($(".collapse").hasClass("in")) {
		$(".collapse").collapse("hide");
	}
	return false;
});


