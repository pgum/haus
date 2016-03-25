var backend_url="/devices"
$(document).ready(function() {
  $.ajax({ url: backend_url}).then(function(data){
    $('.panel').append(data.device_list);
  });
});
