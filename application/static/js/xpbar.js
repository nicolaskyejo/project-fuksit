function flicker(){
  $("#xp-increase-fx-flicker").css("opacity", "1");
  $("#xp-increase-fx-flicker").animate({"opacity":Math.random()}, 100, flicker);
}

$(document).ready(function(){
  flicker();
  doit();
});


