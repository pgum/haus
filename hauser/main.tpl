
<!DOCTYPE html>
<html>
<head>
<style>
.on {
    background-color: #4CAF50;
}
.off {
    background-color: #f44336; 
}
.button {
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
}
.statusbox {
    display: inline-block;
    width: 250px;
    height: 150px;
    margin: 3px;
}
</style>
</head>
<body>
<ul>
<li><a href="/light/0?action=n" class="button on">Light A - ON</a><a href="/light/0?action=f" class="button off">Light A - OFF</a>
<li><a href="/light/1?action=n" class="button on">Light B - ON</a><a href="/light/1?action=f" class="button off">Light B - OFF</a>
<li><a href="/light/3?action=n" class="button on">Light D - ON</a><a href="/light/3?action=f" class="button off">Light D - OFF</a>
</ul>
<ul>
<li><a href="/relay/0?action=n" class="button on">Relay 1 - ON</a><a href="/relay/0?action=f" class="button off">Relay 1 - OFF</a>
<li><a href="/relay/1?action=n" class="button on">Relay 2 - ON</a><a href="/relay/1?action=f" class="button off">Relay 2 - OFF</a>
</ul>
</br>
Last command: {{msg}}

</body>
</html>


