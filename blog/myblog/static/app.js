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

    $("#send-comment").on("click", function() {
        var newComment = $("#commentBodyField").val();
        var request = $.ajax({
            type: "POST",
            data: {
                comment: newComment
            }
        }).done(function(data) {
            console.log(data);
            $("<p>" + data + "</p>").insertAfter("#send-comment");
        });
        return false;
    });
});
