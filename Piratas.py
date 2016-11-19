def answer(numbers):
	bucle = []
	for pirate in numbers:
		if pirate != 0:
			if not pirate in bucle:
				bucle.append(pirate) 
	return len(bucle)

answer([1,2,1])