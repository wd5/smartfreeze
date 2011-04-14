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
					$this.append('<tr class="clone_buy buy"><td></td></tr>');
					$this.find('.first_row').not('.clone_first_row').find('td:first').clone().appendTo($this.find('.clone_first_row'));
					$this.find('.features').not('.clone_first_row').each(function(){
						var i = $(this).index();
						$(this).find('td:first').clone().appendTo($this.find('.clone_feature').eq(i-1));
					});
					//$this.append('<tr><td class="dotted_border_bottom" style="padding-bottom:10px;" colspan="12"></td></tr>');
					while($this.width()>715){
						var $first = $this.find('.clone_first_row td:first');
						var $second = $this.find('.clone_buy td:first');
						$this.find('.first_row').not('.clone_first_row').find('td:last').prependTo($this.find('.clone_first_row'));
						$first.prependTo($this.find('.clone_first_row'));
						$this.find('.features').not('.clone_feature').each(function(){
							var i = $(this).index();
							var $fird = $this.find('.clone_feature').eq(i-1).find('td:first');
							$(this).find('td:last').prependTo($this.find('.clone_feature').eq(i-1));
							$fird.prependTo($this.find('.clone_feature').eq(i-1));
						});
						$this.find('.buy').not('.clone_buy').find('td:last').prependTo($this.find('.clone_buy'));
						$second.prependTo($this.find('.clone_buy'));
					}
				}
			});
		});
	}	
})(jQuery);

