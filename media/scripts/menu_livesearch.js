$(document).ready(function()
{  $('#author_livesearch').livesearch({
		                        searchCallback: authorAjaxSearch,
		                        queryDelay: 200,
		                        innerText: "Search",
		                        minimumSearchLength: 0
	                        });
   $('#tag_livesearch').livesearch({
		                        searchCallback: tagAjaxSearch,
		                        queryDelay: 200,
		                        innerText: "Search",
		                        minimumSearchLength: 0
	                        });
});
