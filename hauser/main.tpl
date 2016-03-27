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

% for device in ('sockets',):
<div class="panel">
  <h2>{{device}}</h2>
  % for name in ('Salon', 'Lampka'):
  <div class="action-wrapper">
    % for action, text in (('switchOn', 'on'), ('switchOff', 'off')):
    <button href="#/{{device}}/{{action}}/{{name}}" class="big clickable {{text}}">{{name}} {{text}}</button>
    % end
    </br>
  </div>
  % end
</div>
% end

<div class="panel">
  <h2>Kodi</h2>
  % for (action, command) in (('Play/Pause','PlayPause'), ('Stop','Stop'), ('Vol-','VolumeDown'),('Vol+','VolumeUp')):
  <button id="kodi-{{command}}" href="#/kodi/{{command}}" class="box clickable twice-big gray">{{action}}</button>
  %end
<input>
</div>
<div class="panel ajaks">
  <h2> Status </h2>
    <div class= "box small"></div>
</div>

</body>
</html>

