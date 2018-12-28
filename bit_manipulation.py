def str_to_bits(string):
    result = []
    for char in string:
        bits = bin(ord(char))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(bit) for bit in bits])
    return result


def str_from_bits(bits):
    chars = []
    for bit in range(len(bits) // 8):
        byte = bits[bit*8:(bit+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)


def int_to_bits(integer, bit_shape=8):
    digits = []
    while integer:
        digits.append(str(integer % 2))
        integer //= 2
    digits += ['0']*(bit_shape-len(digits))
    digits.reverse()
    return ''.join(digits)
