def conv(n,b):
	n*=2
	tupla=()
	string=""
	while n > 1:
		n//=2
		n2=n%2
		tupla=(str(n2))
	n=len(tupla)-1
	while n > 0:
		string+=tupla[n]
		n-=1
	return string

conv(12,2)
