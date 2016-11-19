def mas_larga(string):
	s = ""
	total = ""
	string2 = string.split(" ")
	for stri in string2:
		if len(s) > len(stri):
			total = s
		else:
			total = stri
	print (total)

mas_larga()
