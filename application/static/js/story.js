$(document).ready(function() {
    $('#robohash').fadeIn(1500);
    let xp = parseInt($('p#points').html()) * 100;
    $('p#points').html(xp);
});

// $(function() {
//    $.ajax(
//        {
//            url: "/leaderboard",
//            type: "GET",
//            dataType: "json",
//            processData: false,
//            success:function(result) {
//                 console.log('Leaderboard GET success')
//            },
//            error: function (error) {
//                 console.log('Leaderboard GET fail')
//                 $('p#points').text("0")
//            }
//        })
// });

