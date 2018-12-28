import PIL.Image
from bit_manipulation import *

text = open('text.txt', 'r')

# Читаем текст...

text = text.read()
text_bits = str_to_bits(text)
text_bits = "".join(map(str, text_bits))
text_position = 0

# Открываем и редактируем изображение

image = PIL.Image.open("image.png")
key_encoded = False  # оставим мета-информацию о файле-источнике
key = int_to_bits(len(text), 18)
key_pos = 0


pixels = image.getdata()
result = []

for pixel in pixels:
    if key_encoded:
        r, g, b = pixel
        r_bits, g_bits, b_bits = int_to_bits(r), int_to_bits(g), int_to_bits(b)

        if len(text_bits) - text_position > 0:
            r_bits = r_bits[:-2] + text_bits[text_position:min(text_position + 2, len(text_bits))]
            text_position += 2

        if len(text_bits) - text_position > 0:
            g_bits = g_bits[:-2] + text_bits[text_position:min(text_position + 2, len(text_bits))]
            text_position += 2

        if len(text_bits) - text_position > 0:
            b_bits = b_bits[:-2] + text_bits[text_position:min(text_position + 2, len(text_bits))]
            text_position += 2
        r, g, b = int(r_bits, 2), int(g_bits, 2), int(b_bits, 2)
        pixel = r, g, b
        result.append(pixel)
    else:
        r, g, b = pixel
        print(r, g, b)
        r_bits, g_bits, b_bits = int_to_bits(r), int_to_bits(g), int_to_bits(b)
        r_bits = r_bits[:-2] + "".join(key[key_pos:key_pos + 2])
        key_pos += 2

        g_bits = g_bits[:-2] + "".join(key[key_pos:key_pos + 2])
        key_pos += 2

        b_bits = b_bits[:-2] + "".join(key[key_pos:key_pos + 2])
        key_pos += 2
        r, g, b = int(r_bits, 2), int(g_bits, 2), int(b_bits, 2)
        print(r, g, b)
        pixel = r, g, b
        result.append(pixel)
        if key_pos >= 18:
            key_encoded = True

if text_position < len(text_bits):
    print("Text is not encoded completely")

result_image = PIL.Image.new(image.mode, image.size)
result_image.putdata(result)
result_image.save("result.png")
