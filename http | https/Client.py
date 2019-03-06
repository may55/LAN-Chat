import requests
import time
from threading import Thread

sema = 1

def receive(user):
	res = requests.get('http://127.0.0.1:1998', params=user)
	rec_msgs = res.text

	for msgs in rec_msgs.split(','):
		if len(msgs) > 3:
			user, msg = msgs.split(':')
			print("From", user, ":", msg)

def send():
	while True:
		if sema == 0:
			return

		txt = str(input())

		if txt == "{quit}":
			return

		requests.post('http://127.0.0.1:1998', params=user, data=txt, headers={'Content-Length': str(len(txt))})

user = str(input())

Send_Thread = Thread(target = send)

Send_Thread.start()

while True:
	receive(user)
	try:
		time.sleep(1)

	except KeyboardInterrupt:
		sema = 0
		break

Send_Thread.join()