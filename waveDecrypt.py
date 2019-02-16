import wave
import bit_manipulation

encryptedWave = wave.open("result.wav")
waveBytes = encryptedWave.readframes(encryptedWave.getnframes())
key = ""
key_decrypted = False


textBits = ""
text = ""


for frame in waveBytes:
    if not key_decrypted:
        print(frame)
        key += bit_manipulation.int_to_bits(int(frame))[-1:]
        if len(key) >= 18:
            key = int(key, 2)
            print(key)
            key_decrypted = True
    else:
        textBits += bit_manipulation.int_to_bits(int(frame))[-1:]
        if len(text) >= key:
            break

text = bit_manipulation.str_from_bits(textBits)

file = open('output.txt', 'w')
file.write(text)
file.close()

