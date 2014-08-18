/* globals $, console, document, window */

// $("#loading-example-btn").click(function() {
//     var btn = $(this);
//     btn.button("loading");
//     // $.ajax().always(function() {
//     //     tn.button("reset");
//     // });
//     alert("HHEHHEHEHEHY");
// });

$(document).ready(function() {
    "use strict";

    function goBack() {
        window.history.back();
    }

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
});
