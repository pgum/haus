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
% for (i,name) in ((2,'A'),(4,'B'),(5,'D')):
<a href="/sockets/switchOn/{{i}}" class="box clickable big on">Light {{name}} - ON</a><a href="/sockets/switchOff/{{i}}" class="box clickable big off">Light {{name}} - OFF</a></br>
% end
<h2>Relays</h2>
% for (i,name) in ((0,'1'),(1,'2')):
<a href="/relays/switchOn/{{i}}" class="box clickable big on">Relay {{name}} - ON</a><a href="/relays/switchOff/{{i}}" class="box clickable big off">Relay {{name}} - OFF</a></br>
% end
</div>
% if defined('status'):
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
% end
</div>

<div class="gray container">
<div class="panel">
<h2>Kodi</h2>
% for (action, command) in (('Play/Pause','PlayPause'), ('Vol+','VolumeUp'),('Vol-','VolumeDown')):
<a href="/kodi/{{command}}" class="box clickable twice-big on gray">{{action}}</a>
%end
%if defined('responses'):
</div>
</div>

<div class="gray container">
<div class="panel">
<h2>Kodi</h2>
<h3>{{msg}}</h3>
</div>
</div>
</body>
</html>


