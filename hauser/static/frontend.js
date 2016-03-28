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
  $(function() {
    $( "#allAvailableComamnds" ).menu();
      $.ajax({ url: "self/getAvailableCommands",
               type: 'GET',
               success: function(data){
                              console.log('success',data);
                              $.each(data.message, function(k,v){
                                var methods="";
                                for (index = 0; index < v.length; ++index) {
                                  methods=methods+"<li class=\"devac\" href=\""+k+"/"+v[index]+"\">"+v[index]+"</li>"
                                }
                                $("#allAvailableCommands").append("<li class=\""+k+"\">"+k+"<ul>"+methods+"</ul></li>").on('click','.devac',function(){
$(".command").val($(this).attr('href'));
});
                              });
               },
               error: function(exception){ alert('Exception: ' + exception); }
      });
  });
    $( "#lastPlayed" ).menu();
    $( "#lastPlayed" ).on('click', "li",function(){
      console.log('li clicked');
      hreflink= $(this).attr('href').substring(1);
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink);},
               error: function(exception){alert('Exception: ' + exception);}
      });
    });
    
    $.ajax({ url: "kodi/getLastPlayed",
             type: 'GET',
             success: function(data){
                                      console.log('success',data);
                                      var index;
                                      var a = data.message.lastPlayed;
                                      var uniqIds = [];
                                      $.each(a, function(i, el){
                                        if($.inArray(el,uniqIds) === -1) uniqIds.push(el);
                                      });
                                      for (index = 0; index < uniqIds.length; ++index) {
                                        console.log(uniqIds[index]);
                                        $('#lastPlayed').append("<li href=\"#/kodi/PlayYoutube/"+uniqIds[index]+"\">"+uniqIds[index]+"</li>");
                                      }
                                      $("#lastPlayed").menu( "refresh" );
                                    },
             error: function(exception){alert('Exception: ' + exception);}
    });
    $( ".clickable").button({icons: {primary: 'ui-icon-gear'}});
    $( "#kodi-playYTurl" ).button({text: true, icons: {primary: "ui-icon-play"}});
    $( "#kodi-PlayPause" ).button({text: false, icons: {primary: "ui-icon-play"}});
    $( "#kodi-Stop" ).button({text: false, icons: {primary: "ui-icon-stop"}});
    $( "#kodi-VolumeUp" ).button({text: false, icons: {primary: "ui-icon-volume-on"}});
    $( "#kodi-VolumeDown" ).button({text: false, icons: {primary: "ui-icon-volume-off"}});
    function updatePlayedList(){

}
    $( '.yturl').bind('input',function(){
      var maybeId= YouTubeGetID($(this).val());
      if(maybeId.length==11){
        hreflink= "kodi/PlayYoutube/"+ maybeId;
        $.ajax({ url: hreflink,
                 type: 'GET',
                 success: function(data){
                                          console.log('success',data);
                                          appendMsg(data, hreflink);
                                          $('.yturl').val("");
                                         $('#lastPlayed').append("<li href=\"#/kodi/PlayYoutube/"+maybeId+"\">"+maybeId+"</li>");
                                        },
                 error: function(exception){alert('Exception: ' + exception);}
        });
      }
    });
      function appendMsg(data, hreflink){
      $('#msgs').append(genEventResponse(data, hreflink));
      $("#msgs").accordion( "refresh" );
      $("#msgs").accordion( "option", "active", -1);
      }
    $("#send-cmd").click(function(){
      console.log('sending command');
      hreflink= $('.command').val();
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink);},
               error: function(exception){alert('Exception: ' + exception);}
      });
    });
    $(".device").click(function(){
      console.log('device clicked');
      hreflink= $(this).attr('href').substring(1);
      $.ajax({ url: hreflink,
               type: 'GET',
               success: function(data){ console.log('success',data); appendMsg(data, hreflink);},
               error: function(exception){alert('Exception: ' + exception);}
      });
    });
  });
});
