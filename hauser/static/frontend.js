var backend_url="self/getAvailableCommands"

function genEventResponse(data, hreflink){
var d = new Date();
var godzina= d.toTimeString().substring(0,8);
  return "<h4 style=\"font-size:14px\">"+godzina+" "+hreflink +" "+ data.result+"</h4>" +
         "<pre style=\"font-size:12px\">"+ JSON.stringify(data, undefined, 2) + "</pre>"
}
function YouTubeGetID(url){
  var ID = '';
  url = url.replace(/(>|<)/gi,'').split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/);
  if(url[2] !== undefined) {
    ID = url[2].split(/[^0-9a-z_\-]/i);
    ID = ID[0];
  }
  else {
    ID = url;
  }
    return ID;
}

$(document).ready(function() {
  $(function () {
    $("#msgs").accordion();
    $("#spinner").spinner();
    $( "#slider" ).slider({
      stop: function( event, ui ) {
      hreflink= "kodi/VolumeTo/"+ ui.value;
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink); },
               error: function(exception){alert('Exception: ' + exception);}
      });
}
    });
//$(".panel").draggable();
    $(".clickable").button({icons: {primary: 'ui-icon-gear'}});
    $( "#kodi-playYTurl" ).button({text: true, icons: {primary: "ui-icon-play"}});
    $( "#kodi-PlayPause" ).button({text: false, icons: {primary: "ui-icon-play"}});
    $( "#kodi-Stop" ).button({text: false, icons: {primary: "ui-icon-stop"}});
    $( "#kodi-VolumeUp" ).button({text: false, icons: {primary: "ui-icon-volume-on"}});
    $( "#kodi-VolumeDown" ).button({text: false, icons: {primary: "ui-icon-volume-off"}});
    $("#kodi-playYTurl").click(function(){
      hreflink= "kodi/PlayYoutube/"+ YouTubeGetID($(".yturl").val());
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink); },
               error: function(exception){alert('Exception: ' + exception);}
      });
    });
      function appendMsg(data, hreflink){
      $('#msgs').append(genEventResponse(data, hreflink));
      $("#msgs").accordion( "refresh" );
      $("#msgs").accordion( "option", "active", -1);
}
    $(".device").click(function(){
      hreflink= $(this).attr('href').substring(1);
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink);},
               error: function(exception){alert('Exception: ' + exception);}
      });
    });
  });
});
