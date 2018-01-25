$(document).ready(function(){

	$('.carousel-clientes').owlCarousel({
		loop:true,
		margin:10,
		responsiveClass:true,
		items:6
	});

	
	$(window).scroll(function(){
		var scroll = $(document).scrollTop();
		var alto = $('#header').height();
		if(scroll > alto){
			$('.content-menu').addClass('stycky');
		}else{
			$('.content-menu').removeClass('stycky');
		}
	})
});

/*if (window.addEventListener) window.addEventListener('DOMMouseScroll', wheel, false);
window.onmousewheel = document.onmousewheel = wheel;

function wheel(event) {
	var delta = 0;
	if (event.wheelDelta) delta = event.wheelDelta / 120;
	else if (event.detail) delta = -event.detail / 3;

	handle(delta);
	if (event.preventDefault) event.preventDefault();
	event.returnValue = false;
}

function handle(delta) {
	var time 	= 800;
	var distance 	= 700;

	$('html, body').stop().animate({
		scrollTop: $(window).scrollTop() - (distance * delta )
	}, time );
}*/

