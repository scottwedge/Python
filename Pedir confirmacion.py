Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor'):
	while True:
		ok = raw_input(prompt)
		if ok in ('s', 'S', 'si', 'Si', 'SI'):
			return True
		if ok in ('n', 'no', 'No', 'NO'):
			return False
		reintentos = reintentos-1
		if reintentos < 0:
			raise IOError('usuario duro')
		print queja

		
>>> pedir_confirmacion('¿Le gusta comer?')
¿Le gusta comer?o
Si o no, por favor
¿Le gusta comer?l
Si o no, por favor
¿Le gusta comer?m
Si o no, por favor
¿Le gusta comer?h
Si o no, por favor
¿Le gusta comer?b

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    pedir_confirmacion('¿Le gusta comer?')
  File "<pyshell#11>", line 10, in pedir_confirmacion
    raise IOError('usuario duro')
IOError: usuario duro
>>> 
