import wave

text = open("text.txt", 'r').read()

waveFile = wave.open("sound.wav", 'wb')

waveFile.setnchannels(2)
waveFile.setframerate(44100)
waveFile.setsampwidth(16)

waveFile.readframes()
waveFile.close()

