$(document).ready(function(){
	$("main").load("main.html");
    //$(".main_button").attr("id", "current_page");
    $("main").attr("id", "main");
	$(".owl-carousel").owlCarousel({
		navigation : false, // показывать кнопки next и prev 
		autoPlay: 3000,
		//slideSpeed : 1000,
		paginationSpeed : 1500,
	 
		items : 1, 
		itemsDesktop : false,
		itemsDesktopSmall : false,
		itemsTablet: false,
		itemsMobile : false
	});
	var owl = $(".owl-carousel").data('owlCarousel');
	owl.destroyControlls();
});

$(".navbar-nav .li").click(function(){
    //$(".navigation_item[id='current_page']").removeAttr("id");
    var page = $("a",this).attr("href");
    //var content_id = page.split('.')[0];
    //$(".content").attr("id", content_id);
    $(".content").load(page);
    //$(this).attr("id", "current_page");
    return false;
});


