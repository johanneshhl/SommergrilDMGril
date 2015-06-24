	

	$("[data-func*='menutoggle']").on('click', function(event) {
		event.preventDefault();
		
		$('nav').toggleClass('open')
		$(this).toggleClass('open')


	});

	  $(function() {
      $('#slides').slidesjs({
        width: 600,
        height: 350,
        pagination: {
      		active: false
      	},
      	navigation: {
      	active: true
      	},
      	play: {
      		active: false,
      		effect: "slide",
      		interval: 5000,
      		auto: true,
      		swap: true,
      		pauseOnHover: false,
      		restartDelay: 2500
   		 }
      });
    });


	$("[data-func*='vis-opskrift']").on('click', function(event) {
		event.preventDefault();
				console.log($(this).attr('data-content'));

		var json = $.parseJSON($(this).attr('data-content'));
		var image = '<img src="' + $(this).children('img').attr('src') + '" />'
		var titel = '<h3>' + json.title + '</h3>';
		var metode = '<p>' + json.metod + '</p>';

		var ingredienser = '<p>';

		for (var i = json.lists.length - 1; i >= 0; i--) {
			
			ingredienser += '<b>'+json.lists[i].title +'</b><br />';
			for (var f = json.lists[i].content.length - 1; f >= 0; f--) {
				ingredienser += json.lists[i].content[f]
				ingredienser += '<br/>'
			};
			if (i >= 1) {
				ingredienser += '<br />'
			};
		};

		ingredienser += '</p>';

		$('body').append('<div class="popup">'+
			'<div class="inner">'+
			'<div data-func="remove-popup" class="button">'+
			'<div class="streg"></div>'+
			'<div class="streg"></div>'+
			'</div>'+
			'<div class="text-box"><div class="row">'+ image +'</div><div class="row">'+ titel + ingredienser + metode +'</div>'+
			'</div>'+	
			'</div>'+
			'<div>'); 

		$("[data-func*='remove-popup']").on('click', function(event) {
			event.preventDefault();
			$(this).parents('div.popup').remove()
		});


	});


	$("[data-func*='vis-produkt']").on('click', function(event) {
		event.preventDefault();
		
		var json = $.parseJSON($(this).attr('data-content'));

		var image = '<img src="' + $(this).children('img').attr('src') + '" />'
		var titel = '<h3>' + json.title + '</h3>';
		var desc = '<p>' + json.desc + '</p>';

		$('body').append('<div class="popup">'+
			'<div class="inner">'+
			'<div data-func="remove-popup" class="button">'+
			'<div class="streg"></div>'+
			'<div class="streg"></div>'+
			'</div>'+
			'<div class="text-box"><div class="row">'+ image +'</div><div class="row">'+ titel + desc +'</div>'+
			'</div>'+	
			'</div>'+
			'<div>'); 

		$("[data-func*='remove-popup']").on('click', function(event) {
			event.preventDefault();
			$(this).parents('div.popup').remove()
		});


	});



	$("[data-func*='showNewsLetterSignUp']").on('click', function(event) {
		event.preventDefault();
		
		popup = '<div class="popup">'+
			'<div class="inner">'+
				'<div data-func="remove-popup" class="button">'+
					'<div class="streg"></div>'+
					'<div class="streg"></div>'+
				'</div>'+
				'<div class="newsletter">'+
					'<h3>Skriv dig up til vores nyhedsbrev</h3>'+
					'<form action="/session/signup" method="post">'+
						'<input name="email" type="email" placeholder="john@doe.com">'+
						'<button type="submit" >Tilmeld</button>'
					'</form>'+
				'</div>'+
				'</div>'+	
			'</div>'+
		'<div>'; 

		$('body').append(popup);
		$("[data-func*='remove-popup']").on('click', function(event) {
			event.preventDefault();
			$(this).parents('div.popup').remove()
		});
	});





$("[data-func*='remove-popup']").on('click', function(event) {
	event.preventDefault();
	$(this).parents('div.popup').remove()
});