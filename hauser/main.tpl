% include('header.tpl')

<div class="controls">
  <div class="panel">
    <h2>Ajax status</h2>
    <div id="ajaxIndicator"></div>
  </div>

% for (title,device,channel,actions) in (('Sockets','sockets',('Salon','Lampka'),(('switchOn','on'),('switchOff','off'))),):
<div class="panel">
  <h2>{{title}}</h2>
  % for name in channel:
  <div class="action-wrapper">
    % for action, text in actions:
    <button href="#/{{device}}/{{action}}/{{name}}" class="box half clickable device {{text}}">{{name}} {{text}}</button>
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
    <input type="text" placeholder="Paste youtube url here" class="yturl"/><br/><br/>
    <div id="slider"></div><br/><br/>
    <ul id="lastPlayed"></ul>
  </div>
</div>

<div class="controls">
  <div class="panel">
    <h2> Dev input</h2>
    <input type="text" class="command" placeholder="<device>/<action>/<channel>"/><button id="send-cmd" class="clickable ">Send</button>
  </div>
  <div class="panel">
    <h2> All available commands</h2>
    <ul id="allAvailableCommands"></ul>
  </div>
</div>

<div class="controls">
  <div class="panel">
    <h2> Log management</h2>
    <button href="#/meta/getLog" class="clickable box device one-third gray">getLog</button>
    <button href="#/meta/rmLog" class="clickable box device one-third gray">rmLog</button>
    <button id="reloadLog" class="one-third gray box">reloadLog</button>
  </div>
  <div class="panel">
    <h2> Messages </h2>
    <div id="msgs" style="width:400px;"></div>
  </div>
</div>

% include('footer.tpl')
