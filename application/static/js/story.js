$(document).ready(function() {
    $('#robohash').fadeIn(1500);
    let xp = parseInt($('p#points').html()) * 100;
    $('p#points').html(xp);

  $.ajax(
       {
           url: "/leaderboard",
           type: "GET",
           dataType: "json",
           processData: false,
           success:function(usernames) {
                console.log('Leaderboard GET success')
                $.each(usernames, function (i, username) {
                    $('#leaderboard').append('<li>&thinsp;' + username[0] + '&emsp;xp ' + username[1] * 100 + '</li>')
                });

           },
           error: function (error) {
                console.log('Leaderboard GET fail')
           }
       })
});

