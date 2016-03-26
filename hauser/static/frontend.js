var backend_url="self/getAvailableCommands"
$(document).ready(function() {
  $.ajax({ url: backend_url,
           type: 'GET',
           success: function(data){ console.log('success',data); $('.ajaks').append(data.result);},
           error: function(exception){alert('Exception: ' + exception);}
  });
  $("a").click(function(){
    $.ajax({ url: $(this).attr('href').substring(1),
             type: 'GET',
             success: function(data){ console.log('success',data); $('.ajaks').append(data.result);},
             error: function(exception){alert('Exception: ' + exception);}
    });
  });

});
