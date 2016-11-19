import pyttsx

engine = pyttsx.init()

engine.setProperty('rate', 100)

def speaker(prompt):
	voices = engine.getProperty('voices')
	voice = voices[1] # Cambiar cuando se agregue diccionario
	engine.setProperty('voice', voice.id)
	engine.say(prompt)
	engine.runAndWait()

speaker("Hola")
