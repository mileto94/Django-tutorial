/* globals $, console, document, window */

$(document).ready(function() {
    "use strict";

    $("#back").on("click", function() {
        window.history.back();
    });

    $(".like").on("click", function() {
        var rated = $("#liked").data("rating");
        rated += 1;
        $("#liked").data("rating", rated);
        console.log($("#liked").data("rating"));
        $("span").text("" + rated);
        var request = $.ajax({
            type: "POST",
            data: {
                id: rated
            },
            dataType: "html"
        });
    });

});
