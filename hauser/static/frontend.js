var backend_url="/self/getAvailableCommands"
$(document).ready(function() {
  $.ajax({ url: backend_url}).then(function(data){
    $('.panel').append(data.message);
  });
});
