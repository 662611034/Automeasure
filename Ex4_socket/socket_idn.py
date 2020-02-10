import socket

# sというインスタンス名でソケットを生成
# AF_INET: IPv4、SOCK_STREAM: TCP通信
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# タイムアウトを2秒に設定
s.settimeout(2)
# 測定器と接続
s.connect(("192.168.0.11", 5025))

s.send("*IDN?\n".encode())
id = s.recv(64)

print(id.decode())

s.close()
