import sl4a
import string
import urllib.request, urllib.parse, urllib.error
from xml.dom import minidom

WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=%s'

def Extraer(dom, parent, child):
	return dom.getElementsByTagName(parent)[0].getElementsByTagName(child)[0].getAttribute('data')

def Datos(location, hl=''):
	url = WEATHER_URL % (urllib.parse.quote(location), hl)
	handler = urllib.request.urlopen(url)
	data = handler.read()
	dom = minidom.parseString(data)
	handler.close()
	data = {}
	weather_dom = dom.getElementsByTagName('weather')[0]
	data['city'] = Extraer(weather_dom, 'forecast_information','city')
	data['temperature'] = Extraer(weather_dom, 'current_conditions','temp_f')
	data['conditions'] = Extraer(weather_dom, 'current_conditions', 'condition')
	dom.unlink()
	return data

def Clima(droid):
	msg = 'No se pudo encontrar la ubicacion del dispositivo'
	location = droid.getLastKnownLocation().result
	location = location.get('gps') or location.get('network')
	if location is not None:
		addresses = droid.geocode(location['latitude'], location['longitude'])
		zipp = addresses.result[0]['postal_code']
		if zipp is not None:
			result = Datos(zipp)
			msg = '%(temperatura)s grados y %(condicion)s, en %(ciudad)s.' % result
	return msg


if __name__ == '__main__':
	droid = sl4a.Android()
	print (Clima(droid))