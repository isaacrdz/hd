$(document).on("ready", inicio)
	function inicio()
	{
		$("#mini-menu").on("click",showMenu);
	}

	function showMenu()
	{
		$("nav").toggle();
	}
