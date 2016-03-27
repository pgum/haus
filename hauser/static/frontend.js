var backend_url="self/getAvailableCommands"

function genEventResponse(data){
  return "<div class=\"event\"><div class=\"event-result\">"+ data.result +"</div><div class=\"event-message\">"+ JSON.stringify(data.message) +"</div><div class=\"event-params\">"+ JSON.stringify(data.params) +"</div></div>"
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
    //$(".panel").draggable();
    $(".clickable").button({icons: {primary: 'ui-icon-gear'}});
    $( "#kodi-PlayPause" ).button({text: false, icons: {primary: "ui-icon-play"}});
    $( "#kodi-Stop" ).button({text: false, icons: {primary: "ui-icon-stop"}});
    $( "#kodi-VolumeUp" ).button({text: false, icons: {primary: "ui-icon-volume-on"}});
    $( "#kodi-VolumeDown" ).button({text: false, icons: {primary: "ui-icon-volume-off"}});

  $("input").change(function(){
    $.ajax({ url: "kodi/PlayYoutube/"+ YouTubeGetID($(this).val()),
             type: 'GET',
             success: function(data){ console.log('success',data); $('.ajaks').append(genEventResponse(data));},
             error: function(exception){alert('Exception: ' + exception);}
    });
  $(this).val("")
});
  $("button").click(function(){
    $.ajax({ url: $(this).attr('href').substring(1),
             type: 'GET',
             success: function(data){ console.log('success',data); $('.ajaks').append(genEventResponse(data));},
             error: function(exception){alert('Exception: ' + exception);}
    });
  });

});
});
