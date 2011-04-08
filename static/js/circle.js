(function($){
	$.fn.circle = function() {
		$(document).ready(function(){
			var check = true;
			var zWidth = ($('.special_slider_product').size())*198;
			//alert(zWidth);
			var $line = $('#special_slider_line');
			$line.css({width:zWidth+'px'});
			$('#arrow_block_right').click(function(){
				check = false;
				var thisWidth = parseFloat($line.css('left'),10);
				if((thisWidth-595)>(-zWidth)){
					$line.animate({left:thisWidth-198},function(){check = true;});
					$('#arrow_block_left').css({opacity:'1'});
				}
				else{
					$(this).css({opacity:'0.4',cursor:'default'});
				}
			});
			$('#arrow_block_left').click(function(){
				check = false;
				var thisWidth = parseFloat($line.css('left'),10);
				if((thisWidth)<(0)){
					$line.animate({left:thisWidth+198},function(){check = true;});
					$('#arrow_block_right').css({opacity:'1'});
				}
				else{
					$(this).css({opacity:'0.4',cursor:'default'});
				}
			});
		});
	}	
})(jQuery);