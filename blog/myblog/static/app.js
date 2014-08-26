/* globals $, console, document, window */

$(document).ready(function() {
    "use strict";

    $("#back").on("click", function(){
        window.history.back();
    });

    $(".like").on("click", function() {
        var rated = $("#liked").data().rating;
        var request = $.ajax({
            type: "POST",
            data: {
                id: rated
            },
            dataType: "html"
        });
    });

    $("#send-comment").on("click", function(){
        
    });

});
