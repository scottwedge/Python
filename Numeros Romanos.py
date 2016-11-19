def conv_romano(n):
	string = ""
	if n < 10:
		if n < 4:
			string = string + ("I"*n)
		elif n == 4:
			string = string + "IV"
		elif n == 5:
			string = string + "V"
		elif n > 5 and n < 9:
			string = string + ("V"+("I"*(n-5)))
		elif n == 9:
			string = string + "IX"
		elif n == 10:
			string = string + "X"

conv_romano(10)
