var main = function(){

	function errorMessage(text_str, text_sm){
    	var errorElement = $('<div class="alert alert-danger"></div>')
        .append('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>')
        .append('<strong>'+text_str+'</strong>'+text_sm);

        return errorElement;
    }

	$('input[type=radio][name=optionsMod]').change(function() {
		var diametr = $('input[type=radio][name=optionsD]:checked').val().split('.')[0];
		var typeConnection = $('input[type=radio][name=optionsT]:checked').val();

		if (this.value == 'SM') {
			var nextConnector = '.connectors-' + diametr + '-SM';
			var nextCabel = '.cabel-' + diametr + '-SM-' + typeConnection;
        }
        else if (this.value == 'MM') {
			var nextConnector = '.connectors-' + diametr + '-MM';
			var nextCabel = '.cabel-' + diametr + '-MM-' + typeConnection;
        }
        $(".connectors.in").removeClass("in");
        $(".cabel.in").removeClass("in");
        $(nextConnector).addClass("in");
        $(nextCabel).addClass("in");
	});

	$('input[type=radio][name=optionsD]').change(function() {
		var mod = $('input[type=radio][name=optionsMod]:checked').val();
		var typeConnection = $('input[type=radio][name=optionsT]:checked').val();
		if (this.value == '2.0') {
			var nextConnector = '.connectors-2-' + mod;
			var nextCabel = '.cabel-2-' + mod + '-' + typeConnection;
        }
        else if (this.value == '3.0') {
			var nextConnector = '.connectors-3-' + mod;
			var nextCabel = '.cabel-3-' + mod + '-' + typeConnection;
        }
        $(".connectors.in").removeClass("in");
        $(".cabel.in").removeClass("in");
        $(nextConnector).addClass("in");
        $(nextCabel).addClass("in");
	});

	$('input[type=radio][name=optionsT]').change(function() {
		var mod = $('input[type=radio][name=optionsMod]:checked').val();
		var diametr = $('input[type=radio][name=optionsD]:checked').val().split('.')[0];
		if (this.value == 'simplex') {
			var nextCabel = '.cabel-' + diametr + '-' + mod + '-simplex';
        }
        else if (this.value == 'duplex') {
			var nextCabel = '.cabel-' + diametr + '-' + mod + '-duplex';
        }
        $(".cabel.in").removeClass("in");
        $(nextCabel).addClass("in");
	});

	$("#calculate-patch").on("click", function() {
		var lenghtCabel = $('#lenght-choice').val();
		if (lenghtCabel == '') {
			$('#lenght-choice').text('1,0');
			lenghtCabel = 1;
		}
		var userPatch = {
			'mod' : $('input[type=radio][name=optionsMod]:checked').val(),
			'diametr' : $('input[type=radio][name=optionsD]:checked').val().split('.')[0],
			'connectorLeft' : $("#connectors-left > .connectors.in option:selected").text(),
			'connectorRight' : $("#connectors-right > .connectors.in option:selected").text(),
			'typeConnection' : $('input[type=radio][name=optionsT]:checked').val(),
			'lenghtCabel' : lenghtCabel,
			'typeCabel' : $('#choice-cabel > .cabel.in option:selected').text()
		};
		$.ajax({
	 			url: '/calculatepatch',
	 			type: 'POST',
	 			contentType: "application/json; charset=utf-8",			
	 			data: JSON.stringify(userPatch),
	 			success: function(response) {
	 				$('.user-patch-line').html(response);
	 			},
	 			error: function(error) {
	 				$('.calculator').append(errorMessage("Ошибка на сервере!","Мы не можем обработать ваш запрос"));
	 			}
 			});
	});
}
$(document).ready(main);
