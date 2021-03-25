// import Cropper from 'cropperjs';

function addCode(tagObj) {  
  var oldData = $("#bconid").val() + "\n" + $(tagObj).attr("data-code");
  $("#bconid").val(oldData);
}
function nscrool(toid){
  $('html, body').animate({
    scrollTop: $("#" + toid).offset().top
  }, 2000);
  
}

// Get the element with id="defaultOpen" and click on it
