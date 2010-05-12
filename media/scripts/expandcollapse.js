function openAll() {
    $('#expand .expandContent:hidden').slideDown('500', function(){
        $triggers = $('#expand .triggerClosed');
        $triggers.removeClass('triggerClosed');
        $triggers.addClass('triggerOpen');});
    return false;
}

function closeAll() {
    $('#expand .expandContent:visible').slideUp('500', function(){
        $triggers = $('#expand .triggerOpen');
        $triggers.removeClass('triggerOpen');
        $triggers.addClass('triggerClosed');});
    return false;
}

function toggle() {
    $trigger = $(this);
    if($trigger.hasClass('triggerOpen'))
        $trigger.siblings('.expandContent').slideUp('500', function(){
            $trigger.removeClass('triggerOpen');
            $trigger.addClass('triggerClosed');});
    else
        $trigger.siblings('.expandContent').slideDown('500', function(){
            $trigger.removeClass('triggerClosed');
            $trigger.addClass('triggerOpen');});
    return false;
}

$(document).ready(function()
{
    $headers = $('#expand h4');
    $('#expand .expandContent').hide();
    $headers.addClass('triggerClosed');
    $headers.attr('title','Show/Hide');
    $headers.wrapInner('<a href="#" />');
    $headers.click(toggle);
    $('#openAllBtn').click(openAll);
    $('#openAllBtn').removeClass('btnHide');
    $('#closeAllBtn').click(closeAll);
    $('#closeAllBtn').removeClass('btnHide');
    
});
