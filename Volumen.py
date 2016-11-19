import pyaudio
import audioop

may = 0

pyaud = pyaudio.PyAudio()

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 1,
    input = True)

while True:
        chunk = stream.read(1024)
        mx = audioop.max(chunk, 2)
        print mx
