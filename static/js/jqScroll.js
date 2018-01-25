$(document).ready(function() {

	
			$(".nav-link").click(function() {
				var header=document.getElementsByClassName("navbar-brand")[0].clientHeight;
    			$("html, body").animate({scrollTop: $("#"+String(this).split("#")[1]).offset().top-header}, 2000);
    		});
				
		

		
  
});