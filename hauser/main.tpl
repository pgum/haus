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
    <button href="#/{{device}}/{{action}}/{{name}}" class="box clickable device {{text}}">{{name}} {{text}}</button>
    % end
    </br>
  </div>
  % end
</div>
% end

<div class="panel">
  <h2>Kodi</h2>
  % for command in ('PlayPause', 'Stop', 'VolumeDown','VolumeUp'):
  <button id="kodi-{{command}}" href="#/kodi/{{command}}" class="box device twice-big gray">{{command}}</button>
  %end
  <input class="yturl"/><button id="kodi-playYTurl">Play</button><br/>
  <div id="slider"></div>
</div>

<div class="panel">
  <h2> Messages </h2>
    <div id="msgs" style="width:400px;"></div>
</div>

</body>
</html>

