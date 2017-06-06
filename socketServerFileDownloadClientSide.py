#coding:utf-8
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("123.206.68.233",8000))
sock.send("Ready for download")
while True:
	sends = raw_input('>>>')
	sock.send(sends)
	if sends == 'break':
		break
	else:		
		with open ('proj.txt', 'w') as f:
			f.write(sock.recv(1024))
		sock.close()
		break

