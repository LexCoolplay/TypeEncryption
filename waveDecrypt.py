import wave

waveRead = wave.open('sound.wav', 'r')
waveBytes = waveRead.readframes(waveRead.getnframes())

file = open('output.txt', 'w')
try:
    file.write(waveBytes.decode('utf-8'))
except UnicodeDecodeError:
    file.close()
