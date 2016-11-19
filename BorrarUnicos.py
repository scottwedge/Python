def borrarunicos():
	i2=0
	checkio=[1,2,3,1,2]
	for i in range(0,len(checkio)):
		while i2 < len(checkio):
			if (checkio[i] == checkio[i2]) & i!=i2:
				break
			i2+=1
		else:
			del(checkio[i])
			print(checkio)
	return checkio

borrarunicos()
