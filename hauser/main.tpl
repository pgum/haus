<!DOCTYPE html>
<html>
<head>
 <head>
 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
 <script src="/static/frontend.js"></script>
 <link type="text/css" rel="stylesheet" href="/static/main.css" />
 <link rel="shortcut icon" href="/static/favicon.ico" />
 </head>
</head>
<body>

<div class="gray container">
  <div class="panel">
    <h2>Sockets</h2>
    % for name in ('Salon', 'Lampka', 'Nieuzywany'):
    <a href="#/sockets/switchOn/{{name}}" class="box clickable big on">{{name}} - ON</a>
    <a href="#/sockets/switchOff/{{name}}" class="box clickable big off">{{name}} - OFF</a></br>
    % end
  </div>
  <div class="panel ajaks">
    <h2> Status </h2>
    <div class="box ">
      <h3> s </h3>
      <div class= "box small "></div>
    </div>
  </div>
</div>

<div class="gray container">
  <div class="panel">
    <h2>Kodi</h2>
    % for (action, command) in (('Play/Pause','PlayPause'), ('Vol+','VolumeUp'),('Vol-','VolumeDown')):
    <a href="#/kodi/{{command}}" class="box clickable twice-big on gray">{{action}}</a>
    %end
  </div>
</div>

</body>
</html>


