import PIL.Image
from bit_manipulation import *


image = PIL.Image.open("result.png")
pixels = image.getdata()

key_decoded = False
key = ""

text = open("result.txt", 'w')
text_result = ""
text_bits = ""

for pixel in pixels:
    if key_decoded:
        r, g, b = pixel
        r_bits, g_bits, b_bits = "", "", ""
        if len(text_bits) < key * 8:
            r_bits = int_to_bits(r)[-2:]
        if len(text_bits) + 2 < key * 8:
            g_bits = int_to_bits(g)[-2:]
        if len(text_bits) + 4 < key * 8:
            b_bits = int_to_bits(b)[-2:]
        text_bits += r_bits + g_bits + b_bits
    else:
        r, g, b = pixel
        print(r, g, b)
        r_bits, g_bits, b_bits = int_to_bits(r)[-2:], int_to_bits(g)[-2:], int_to_bits(b)[-2:]
        key += r_bits + g_bits + b_bits
        if len(key) >= 18:
            key_decoded = True
            key = int(key, 2)

text_result = str_from_bits(text_bits)
text.write(text_result)
