//ADD YOUR CODE HERE.

// Funtion to display tooltip on page load
function showToolTip(content, selector) {
    // Adding a <p> tag to show the tooltip
    $('<p class="tooltip">'+content+'</p>')
        .appendTo(selector);
    // Removing the tooltip after some time
    setTimeout(function(){  $(selector).find('p').remove(); }, 2000);
};

// Main document ready funtion
$(document).ready(function() {
    // Parsing the json that the view forwarded
    var guide1 = JSON.parse(guide);
    for(var i=0, keys=Object.keys(guide1.steps), l=keys.length; i<l; i++)
    {
        // Looping through each element in json and calling teh showToolTip function
        var selector = guide1.steps[i].selector;
        var content = guide1.steps[i].content;
        (function (i) {
            setTimeout(function() { showToolTip(guide1.steps[i].content,
                guide1.steps[i].selector);}, 2000*i);
        })(i);
    }

});