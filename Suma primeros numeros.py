def s1s2(n):
	m = 0
	total1 = 0
	total2 = 0
	for m in range(n+1):
		print (m)
		total1 = total1 + m
	total2 = (n * (n + 1))/2
	print (total1, total2)

s1s2(12)
