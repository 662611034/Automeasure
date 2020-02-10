<?php
$s = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_set_option($s, SOL_SOCKET, SO_SNDTIMEO, array('sec'=>3, 'usec'=>0));
if(socket_connect($s, "192.168.0.11", 5025)){
    $msg = "*IDN?\n";
    socket_write($s, $msg, strlen($msg));
    $id = socket_read($s, 128);
    echo($id);
}
