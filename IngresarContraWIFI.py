def ingcontra():
	from subprocess import Popen,STDOUT, PIPE
	from time import sleep
	handle = Popen('netsh wlan connect WIFI_Name',shell='True', stdout=PIPE, stderr=STDOUT, stdin=PIPE)
	sleep(5)
	handle.stdin.write('Contra\n')

ingcontra()
