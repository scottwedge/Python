def media_armonica(*n):
	n2 = 0
	total = 0
	while n2 < (len(n)):
		total = total + (1/n[n2])
		n2+=1
	total = len(n)/total
	return total

media_armonica(1,2,3,4,5,6)
