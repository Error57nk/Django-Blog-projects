
$(document).ready(function () {

  $("#hamtog").click(function () {
    $(".side-nav").toggleClass("active");
    $(".h-btn").toggleClass("active");
    // $("#ham-icon").removeClass("fa-bars");
    // $("#ham-icon").addClass("fa-times");
  });

  $("#defaultOpen").click();
   
});


// AbutPro
function openSection(evt, secName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(secName).style.display = "block";
  evt.currentTarget.className += " active";
}


function nscrool(toid){
  $('html, body').animate({
    scrollTop: $("#" + toid).offset().top
  }, 2000);
 }





