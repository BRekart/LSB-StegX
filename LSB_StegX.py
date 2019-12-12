from PIL import Image


# The following method takes a given set of bits and 
# appends each characterized section into our 'result' variable.
# It's used in decryption later.

def bits_tostring(data, num_bits):
    result = ''
    accum = 0
    shift = 0

    for bits in data:
        accum = accum + (bits << shift)
        shift += num_bits
        if shift >= 8:  # decoding 8 bits!
            result = result + chr(accum)
            accum = 0
            shift = 0
    return result


def string2bits(in_str, num_bits):
    # Returns a list of n bit values from a string.
    # in_str    the string to generate n bit values from

    encode_mask = 2 ** num_bits - 1

    # get n bits at a time from the string, append to result
    result = []
    for ch in in_str:
        ch_value = ord(ch)  # need an integer value
        for _ in range(8//num_bits):
            result.append(ch_value & encode_mask)
            ch_value = ch_value >> num_bits
    return result


# Now beginning main logic. User given choice to
# encrypt or decrypt.
mode = input("Would you like to [E]ncrypt or [D]ecrypt? \n")
mode = mode.upper()
eoc_marker = "\0"

if mode == 'E':

# Hard-coded currently, so two.bmp must be present within the source folder.
    image = Image.open('two.bmp')
    pixels = list(image.getdata())
# Maximum message length depends on overall size of image.
    plaintext = input("What message would you like to hide? \n")
    plaintext = plaintext + eoc_marker
# Bit-depth choice will help illustrate variance in image degradation.
    num_bits = input("How many bits would you like to encrypt with? (1/2/4/8) \n")
    num_bits = int(num_bits)

    new_pixels = []

    nbit_text = string2bits(plaintext, num_bits)

    while len(nbit_text) % 3:
        nbit_text.append(0)
    encode_iter = iter(nbit_text)
    nbit_tuples = []
    for x in encode_iter:
        nbit_tuples.append((x, next(encode_iter), next(encode_iter)))
    # Here, we begin encoding into the pixels themselves.
    encode_mask = (2 ** num_bits - 1) ^ 0b11111111
    for (pix, nbits) in zip(pixels, nbit_tuples):
        (r, g, b) = pix
        (e_r, e_g, e_b) = nbits
        new_r = (r & encode_mask) | e_r
        new_g = (g & encode_mask) | e_g
        new_b = (b & encode_mask) | e_b
        new_pixels.append((new_r, new_g, new_b))
# Note that we save into two_encoded.bmp.
    image.putdata(new_pixels)
    image.save('two_encoded.bmp')
    print("[E]ncoding complete.")

if mode == 'D':
# Decrypting from our saved two.encoded.bmp.
    image_encoded = Image.open('two_encoded.bmp')
    pixels_encoded = list(image_encoded.getdata())

    decoded_pixels = []

    num_bits = input("How many bits would you like to decrypt with? (1-8)\n")
    num_bits = int(num_bits)

    decode_mask = 2 ** num_bits - 1
    for (pix_encoded) in pixels_encoded:
        (r_e, g_e, b_e) = pix_encoded
        r_decoded = r_e & decode_mask
        g_decoded = g_e & decode_mask
        b_decoded = b_e & decode_mask

        decoded_pixels.append(r_decoded)
        decoded_pixels.append(g_decoded)
        decoded_pixels.append(b_decoded)
        if eoc_marker in bits_tostring(decoded_pixels,num_bits):
            break

    decoded_bits = bits_tostring(decoded_pixels, num_bits)  # called only once
    print(decoded_bits)
	
