def max_in_list(*arb):
	s = 0
	total = 0
	for string in arb:
		if s > string:
			total = s
		else:
			total = string
		s = string
	print (total)

max_in_list(1,2,3)
