import wave

sound = wave.open('sound.wav', 'r')
source = wave.open('source.wav', 'r')

interfereResult = wave.open('result.wav', 'w')

interfereResult.setnchannels(source.getnchannels())
interfereResult.setframerate(source.getframerate())
interfereResult.setsampwidth(source.getsampwidth())

unwrittenSound = sound.getnframes()
unwrittenSource = source.getnframes()

# Оставляем мета-данные
if(unwrittenSound >= unwrittenSource):
    print("Sound must be shorter than Source!")
    raise SystemExit
else:
    key = (unwrittenSource+unwrittenSound-1)//unwrittenSound
    encryptedKey = (str(key)).encode('utf-8') # sound < source (optimal)

interfereResult.writeframes(encryptedKey)

for index in range(unwrittenSound+unwrittenSource//key):
        interfereResult.writeframes(sound.readframes(1))
        interfereResult.writeframes(source.readframes(key))

interfereResult.close()
