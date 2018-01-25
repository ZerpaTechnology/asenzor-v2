

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}


$(document).ready(function(){

	$('.owl-carousel').owlCarousel({
		items:1,
		autoplay:true,
		//loop:true,
	});

	$.stellar({
		horizontalScrolling: false,
		responsive: true
	});

	
	 $.RDParallax();

	 var swiper = new Swiper('.swiper-container',{
	 	pagination:'.swiper-pagination',
	 	slidesPerView:2,
	 	spaceBetween:5,
	 	
	 });

	 $('.test-popup-link').magnificPopup({
		  type: 'image'
		  // other options
	});

	$('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');

      if (target.length) {
      	

        $('html, body').animate({
          scrollTop: target.offset().top-180
        }, 1000);
        if(this.hash.slice(1)=="about"){
        	sleep(160);
        	$("#about").addClass("animated fadeInUp");
        }
        else{
        	$("#about").removeClass("animated fadeInUp");
        }

        return false;
      }
    }
  });

	/*$(window).scroll(function(){
		var scroll = $(document).scrollTop();
		var header = $('header').height();
		
		if(scroll > header){
			$('.content-menu').addClass('stycky');
		}else{
			$('.content-menu').removeClass('stycky');
		}
		
	});*/

});

