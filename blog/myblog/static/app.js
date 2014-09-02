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

    $("#right").click(function() {
        var currentSlide = $(".active");
        var nextSlide = currentSlide.next();

        if(nextSlide.length === 0) {
            nextSlide = $(".item").first();
        }
        currentSlide.fadeOut(500).removeClass("active");
        nextSlide.fadeIn(500).addClass("active");
    });

    $("#left").click(function() {
        var currentSlide = $(".active");
        var prevSlide = currentSlide.prev();

        if(prevSlide.length === 0) {
            prevSlide = $(".item").last();
        }

        currentSlide.fadeOut(500).removeClass("active");
        prevSlide.fadeIn(500).addClass("active");
    });



});
