import wave

text = open("text.txt", 'r').read()

waveFile = wave.open("sound.wav", 'wb')

waveFile.setnchannels(2)
waveFile.setframerate(256)
waveFile.setsampwidth(2)

waveFile.writeframes(text.encode("utf-8"))

waveFile.close()
