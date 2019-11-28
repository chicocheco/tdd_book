// declare an object as property of the window global and make our function an attribute
window.SuperLists = {};
window.SuperLists.initialize = function () {
    // .on() means “when the following event occurs"
    $('input[name="text"]').on('keypress focus', function () {
        $('.has-error').hide();
    });
};