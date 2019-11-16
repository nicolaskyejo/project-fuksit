$(document).ready(function() {
    $('#robohash').fadeIn(1500);
    let xp = parseInt($('p#points').html()) * 100;
    $('p#points').html(xp);

    $('#logout').click(function(){
        let reallyLogout = confirm("Do you really want to log out? Points will be flushed");
        if(reallyLogout) {
            location.href="/logout";
        }
    });

    getLeaderboard();
});

setInterval(getLeaderboard, 15000);
function getLeaderboard() {
  $.ajax(
       {
           url: "/leaderboard",
           type: "GET",
           dataType: "json",
           processData: false,
           success:function(usernames) {
                console.log('Leaderboard GET success')
                $('#leaderboard > tbody').empty();
                $.each(usernames, function (i, username) {
                    $('#leaderboard > tbody').append('<tr class="table-active"><th scope="row">' + (i+1) + '</th>' +
                        '<td>' + username[0] + '</td><td>' + username[1] * 100 + '</td></tr>');
                });
           },
           error: function (error) {
                console.log('Leaderboard GET fail')
           }
       })
}
