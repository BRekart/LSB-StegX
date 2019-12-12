# LSB-StegX
Python program allowing users to encrypt and decrypt into an image using least-significant bit image steganography.

I've provided a sample pixel image, "two.bmp", here to download. Make sure this is in the same folder as LSB_StegX.py.

ENCRYPTION:
Upon running the .py script, you'll be given a prompt allowing you to choose encryption or decryption. If you choose to encrypt, you can then enter a string or a message of some sort.

You will then choose a bit-depth. This corresponds to how many bits out of every byte will be used for encryption. If larger images are used (although we're using two.bmp, a very small image, here) anything above 2 bits out of every byte will noticeably degrade the image.

The program will close, and a new image will be placed in the source folder. This image contains your steganographic encryption.

DECRYPTION: To decrypt, make sure you've opened this .py file from an already existing command line interface, otherwise the program will close too fast to read the decrypted message.

Same process as encryption, it will decode our saved image ("two_encoded.bmp") and print out the hidden message. Make sure to choose the same number of bits as you chose to encrypt!
