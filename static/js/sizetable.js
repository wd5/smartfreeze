(function($){
	$.fn.sizetable = function() {
		$(document).ready(function(){
		setResize();
		$(window).bind('resize',setResize);			
		});
		function setResize(){
			var best_areawidth = $('#best_sellers').width();
			//количество товара 1 строку			
			var col_inline = (best_areawidth-(best_areawidth%198))/198;
			var col_real = $('.best_product').size();
			if(col_real<col_inline){
				col_inline = col_real;
				var margin1 = (best_areawidth-(col_inline*198))/(col_inline*2)-1;
				$('.best_product').css({margin:'10px '+margin1+'px'});
			}
			else{
				var margin1 = (best_areawidth-(col_inline*198))/(col_inline*2)-1;
				$('.best_product').css({margin:'10px '+margin1+'px'});
				var lost_col = col_real%col_inline;
				var margin_lost = (best_areawidth-(lost_col*198))/(lost_col*2)-1;
				var i;
				for(i=1; i<lost_col+1; i=i+1){
					//alert(col_real);
					$('.best_product').eq(col_real-i).css({margin:'0 '+margin_lost+'px'});
				}
			}
			
			var best_areawidth1 = $('#content').width();
			
			//количество товара 1 строку			
			var col_inline1 = (best_areawidth1-(best_areawidth1%173))/173;
			var col_real1 = $('.cats_prew_block').size();
			if(col_real1<col_inline1){
				col_inline1 = col_real1;
				var margin2 = (best_areawidth1-(col_inline1*173))/(col_inline1*2)-1;
				$('.cats_prew_block').css({margin:'10px '+margin2+'px'});
			}
			else{
				var margin2 = (best_areawidth1-(col_inline1*173))/(col_inline1*2)-1;
				$('.cats_prew_block').css({margin:'10px '+margin2+'px'});
				var lost_col1 = col_real1%col_inline1;
				var margin_lost1 = (best_areawidth1-(lost_col1*173))/(lost_col1*2)-1;
				var i1;
				for(i1=1; i1<lost_col1+1; i1=i1+1){
					//alert(col_real);
					$('.cats_prew_block').eq(col_real1-i1).css({margin:'0 '+margin_lost1+'px'});
				}
			}
		}
	}	
})(jQuery);
