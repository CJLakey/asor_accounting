$(document).on('click', '.count-selector', function(){
    let type = $(this).attr('data-selector-type');
    let cash_selector = $('.count-selector[data-selector-type="cash"]');
    let check_selector = $('.count-selector[data-selector-type="check"]');
    console.log(type);
    if(type === 'cash'){
        check_selector.css({"background" : "", "color" : ""})
        cash_selector.css({"background" : "#2c3034", "color" : "#fff"})
        $('.cash-count-container').show();
        $('.check-count-container').hide();

    } else {
        cash_selector.css({"background" : "", "color" : ""})
        check_selector.css({"background" : "#2c3034", "color" : "#fff"})
        $('.check-count-container').show();
        $('.cash-count-container').hide();
    }
});

