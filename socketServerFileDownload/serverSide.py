#!/usr/bin/python
#coding:utf-8
import os
import json
import time
import threading
import SocketServer

def take_hander(file_path,code="utf-8"):
	file_name_list = file_path.rsplit(os.sep, 1)
	if len(file_name_list) > 1:
		file_name = file_name_list[1]
	else:
		file_name = file_path
	file_size = os.path.getsize(file_path)
	date = time.ctme()
	head_data = {"file_name":file_name,
				"file_size":file_size,
				"date":date,
				"charset":code
				}
	file_header = json.dumps(head_data)
	return head_data
path = "proj.txt"

class Myhandler(SocketServer.BaseRequestHandler):
	def setup(self):
		self.file = open(path,"r")
		self.content = self.file.read()
		#self.file_header = take_hander(path)
		#self.request.sendall(self.file_header)
	def handle(self):
		#self.client_address
		conn = self.request
		print('do you want to download proj.txt ?')
		while True:
			confirm = conn.recv(1024)
			if confirm == 'n':
				print 'Abort download'
				break
			if confirm == 'y':
				conn.sendall('starting dowload')
				print("%s:%s is connected"%self.client_address)
				request_data = self.request.recv(512)
				print(request_data)
				#self.request.sendall(self.file_header)
				#print(file_header)
				self.request.sendall(self.content)
				print 'download complete'
				break

			#else:
				#conn.sendall('confirm again')
			#print '%s:%s is send %s' % (self.client_address[0],self.client_address[1],data)
		
	def finish(self):
		print("%s is done"%self.client_address[0])
		if self.file.closed == False:
			self.file.close()

class Myserver(SocketServer.TCPServer,SocketServer.ThreadingMixIn):
	pass
m = Myserver(("",8000),Myhandler)
th = threading.Thread(target=m.serve_forever(),args=())
th.start()
m.shutdown()
m.server_close()
