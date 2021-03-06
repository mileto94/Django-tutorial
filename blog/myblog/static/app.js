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

    var right = function() {
        var currentSlide = $(".active-slide");
        var nextSlide = currentSlide.next();

        if(nextSlide.length === 0) {
            nextSlide = $(".item").first();
        }
        currentSlide.hide(600).removeClass("active-slide");
        nextSlide.show(300).addClass("active-slide");

        var currentDot = $(".active-dot");
        var nextDot = currentDot.next();

        if(nextDot.length === 0) {
            nextDot = $(".dot").first();
        }

        currentDot.removeClass("active-dot");
        nextDot.addClass("active-dot");
    };

    $("#right").click(right);


    var left = function() {
        var currentSlide = $(".active-slide");
        var prevSlide = currentSlide.prev();

        if(prevSlide.length === 0) {
            prevSlide = $(".item").last();
        }

        currentSlide.hide(600).removeClass("active-slide");
        prevSlide.show(600).addClass("active-slide");

        var currentDot = $(".active-dot");
        var prevDot = currentDot.prev();

        if(prevDot.length === 0) {
            prevDot = $(".dot").last();
        }

        currentDot.removeClass("active-dot");
        prevDot.addClass("active-dot");
    };

    $("#left").click(left);

    setInterval(function(){
        $("#right").trigger("click");
    }, 5000);

    $(".btn").hover(function() {
        $(this).css("cursor", "pointer");
    });

    $(".dropdown").click(function(){
        $('.dropdown-menu').toggle();
    });

});
