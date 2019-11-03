$(document).ready(function() {
    $('#robohash').fadeIn(1500);
    let xp = parseInt($('p#points').html()) * 10;
    $('p#points').html(xp);
});

// $(function() {
//    $.ajax(
//        {
//            url: "/points?username=testuser",
//            type: "GET",
//            dataType: "json",
//            processData: false,
//            success:function(result) {
//                 console.log('GET success')
//                 let xp = result.points * 10;
//                 $('p#points').text(xp)
//            },
//            error: function (error) {
//                 console.log('GET fail')
//                 $('p#points').text("0")
//            }
//        })
// });

