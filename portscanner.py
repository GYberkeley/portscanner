import socket
import os


localIP = socket.gethostbyname(socket.gethostname())


localDevices = []

def findLocalFriends(message, localAddress = localIP):
	"""

	I am making an assumption here that all the LAN connections are between ports 1 and 1000.

	"""
	currentDir = os.getcwd()
	f = open(currentDir + "/output.txt", 'w')
	f.write(message)


	try:
		for port in range(1, 1000):

			                  # IPv4          # TCP Connections
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			# connects to a remote socket address and returns a 0 for error or 1 for success
			connectionTrue = s.connect_ex((localAddress, port))

			if connectionTrue:
				s.connect((localAddress, port))
				localDevices.append(s.gethostname())

				# sending messages to all friends in the local network
				s.send(message)
				s.close()

		f.close()

	except socket.error:
		print("Server couldn't connect")