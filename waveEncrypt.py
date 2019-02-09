import wave
import bit_manipulation

waveRead = wave.open('sound.wav', 'r')
waveBytes = waveRead.readframes(waveRead.getnframes())

text = open('text.txt', 'r')

# Читаем текст...

text = text.read()
text_bits = bit_manipulation.str_to_bits(text)
text_bits = "".join(map(str, text_bits))
text_position = 0

key_encoded = False  # оставим мета-информацию о файле-источнике
key = bit_manipulation.int_to_bits(len(text), 18)
key_pos = 0


for frame in waveBytes:
    if key_encoded:
        frame = int(bit_manipulation.int_to_bits(int(frame))[:-1] + text_bits[text_position], 2)
        text_position += 1
    else:
        if key_pos < 18:
            frame = int(bit_manipulation.int_to_bits(int(frame))[:-1] + key[key_pos], 2)
            key_pos += 1
        else:
            key_encoded = True

file = open('output.txt', 'w')
waveRead.writeframes(waveBytes)

try:
    file.write(waveBytes.decode('utf-8'))
except UnicodeDecodeError:
    file.close()
