require 'socket'

hostname = '192.168.0.11'
port = 5025

sock = TCPSocket.open(hostname, port)

sock.write("*IDN?\n")
puts sock.recv(256)
# puts sock.gets

sock.close
