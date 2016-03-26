<!DOCTYPE html>
<html>
<head>
 <head>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
 <script src="/static/jquery-ui.js"></script>
 <script src="/static/frontend.js"></script>
 <link type="text/css" rel="stylesheet" href="/static/jquery-ui.css" />
 <link type="text/css" rel="stylesheet" href="/static/main.css" />
 <link rel="shortcut icon" href="/static/favicon.ico" />
 </head>
</head>
<body>

<div class="gray container">
  <div class="panel">
    <h2>Sockets</h2>
    % for name in ('Salon', 'Lampka', 'Nieuzywany'):
    <a href="/sockets/switchOn/{{name}}" class="box clickable big on">{{name}} - ON</a>
    <a href="/sockets/switchOff/{{name}}" class="box clickable big off">{{name}} - OFF</a></br>
    % end
  </div>
  <div class="panel">
    <h2> Status </h2>
    %  import simplejson as json
    %  status= json.loads(get('status'))
    %  for dev in status.keys():
    <div class="box {{dev}}">
      <h3> {{dev.title()}}s </h3>
      %   for channel_status in status[dev]:
      <div class= "box small {{channel_status}}"></div>
      %   end
    </div>
    %  end
  </div>
</div>

<div class="gray container">
  <div class="panel">
    <h2>Kodi</h2>
    % for (action, command) in (('Play/Pause','PlayPause'), ('Vol+','VolumeUp'),('Vol-','VolumeDown')):
    <a href="/kodi/{{command}}" class="box clickable twice-big on gray">{{action}}</a>
    %end
  </div>
</div>

<div class="gray container testowy">
  <div class="panel" id="ajaxtest1">
  <h2>Ajaxtest1</h2>
  <h3>tekst</h3>
  </div>
</div>

</body>
</html>


