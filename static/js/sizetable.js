(function($){
	$.fn.sizetable = function() {
		$(document).ready(function(){
			$('.product_dscr_table').each(function(){
				var $this = $(this);
				if($this.width()>715){
					$this.append('<tr class="clone_first_row first_row"></tr>');
					$this.find('.features').each(function(){
						$this.append('<tr class="clone_feature features"></tr>');
					});
					$this.append('<tr class="clone_buy buy"></tr>');
					$this.find('.first_row').not('.clone_first_row').find('td:first').clone().appendTo($this.find('.clone_first_row'));
					$this.find('.features').not('.clone_first_row').each(function(){
						var i = $(this).index();
						$(this).find('td:first').clone().appendTo($this.find('.clone_feature').eq(i-1));
					});
					//$this.append('<tr><td class="dotted_border_bottom" style="padding-bottom:10px;" colspan="12"></td></tr>');
					while($this.width()>715){
						$this.find('.first_row').not('.clone_first_row').find('td:last').appendTo($this.find('.clone_first_row'));
						$this.find('.features').not('.clone_feature').each(function(){
							var i = $(this).index();
							$(this).find('td:last').appendTo($this.find('.clone_feature').eq(i-1));
						});
						$this.find('.buy').not('.clone_buy').find('td:last').appendTo($this.find('.clone_buy'));
					}
				}
			});
		});
	}	
})(jQuery);

