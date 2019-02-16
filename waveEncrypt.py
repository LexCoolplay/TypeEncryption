import wave
import bit_manipulation

waveRead = wave.open('sound.wav', 'r')
waveBits = waveRead.readframes(waveRead.getnframes())

text = open('text.txt', 'r')

# Читаем текст...

text = text.read()
text_bits = bit_manipulation.str_to_bits(text)
text_bits = "".join(map(str, text_bits))
text_position = 0

key_encoded = False  # оставим мета-информацию о файле-источнике
key = bit_manipulation.int_to_bits(len(text), 18)
key_pos = 0
newBits = []

for frame in waveBits:
    if key_encoded:
        frame = int(bit_manipulation.int_to_bits(int(frame))[:-1] + text_bits[text_position], 2)
        # print(frame)
        newBits = [frame, *newBits]
        text_position += 1
    else:
        if key_pos < 18:
            frame = int(bit_manipulation.int_to_bits(int(frame))[:-1] + key[key_pos], 2)
            newBits = [frame, *newBits]
            key_pos += 1
        else:
            key_encoded = True

newBits.reverse()

for frame in newBits:
    print(frame)

file = open('output.txt', 'w')

waveWrite = wave.open("result.wav", 'wb')
waveWrite.setnchannels(waveRead.getnchannels())
waveWrite.setsampwidth(waveRead.getsampwidth())
waveWrite.setframerate(waveRead.getframerate())

print(int(key, 2))

waveWrite.writeframes(bytes(newBits))
waveWrite.close()
