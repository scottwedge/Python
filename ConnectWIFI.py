def connectWIFI():
	from subprocess import check_output
	output = check_output('netsh wlan connect _Wifi_name_', shell=True)
	print output

connectWIFI()
