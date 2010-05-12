var timeout    = 300;
var closetimer = 0;
var menuitem = 0;

function list_menu_click()
{
    $b = $(this).parent();
    $s = $b.siblings();
    if ($b.hasClass('selected'))
    {
        $b.find('div:visible').slideUp('500', function(){$b.removeClass('selected');});
    } else {
        $s.find('div:visible').slideUp('500', function(){$s.removeClass('selected');});
        $b.find('div:hidden').slideDown('500');
        $b.addClass('selected');
    }
    return false;
}

$(document).ready(function()
{   $('#list_menu > li > a').click(list_menu_click);
    $('#list_menu>li>div').hide();});

$(document).click(function(event)
{   $target = $(event.target);
    if ($target.closest('#list_menu').size()==0)
    {
        $vis = $('#list_menu div:visible');
        $vis.slideUp('500', function(){$vis.parent().removeClass('selected');});
    }
});
