<!DOCTYPE html>
<html>
<head>
 <head>
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
%if defined('msg'):
<div class="panel">
<h2>Last command to uC</h2>
<h3>{{msg}}</h3>
</div>
%end
%if defined('responses'):
<div class="panel">
<h2>Responses from uC</h2>
% for response in responses:
<h3>{{response}}</h3>
% end
</div>
%end
</div>

</body>
</html>


