function main() {
	$('.advertising a').click(function(){
		$(".content").attr("id", "equipments");
		$(".content").load("/equipments");
		var currentPage = $('.navbar-nav > li.active');
		var nextPage = currentPage.next();
		currentPage.removeClass("active");
		nextPage.addClass("active");
		return false;
	});
}

$(document).ready(main);