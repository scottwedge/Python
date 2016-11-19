import threading

def finish():
	print "Finished"
	raw_input()

t = threading.Timer(5.0, finish)
t.start()