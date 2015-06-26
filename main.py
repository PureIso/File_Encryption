__author__ = 'pureisometric'
import sys
from Crypto.Cipher import DES3

"""
File Encryption using pycrypto : https://github.com/dlitz/pycrypto/releases
Install - pycrypto
pip install pycrypto
"""


def main():
    mode = sys.argv[1]          # The action - decrypt or encrypt
    file_path = sys.argv[2]     # The file path
    key = sys.argv[3]           # The password
    iv = "A0B1CDEF"             # IV has to be the same for encryption and decryption
    chunk_size = 8192

    if mode == 'encrypt':
        des = DES3.new(key, DES3.MODE_CFB, iv)
        # Initialise variables
        in_filename = file_path
        out_filename = in_filename + ".encrypted"
        # with will close the io on exit
        # initialise the file to read
        with open(in_filename, 'r') as in_file:
            # initialise the file to write
            with open(out_filename, 'w') as out_file:
                while True:
                    # read the chuck_size worth of data
                    chunk = in_file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += ' ' * (16 - len(chunk) % 16)
                        # encrypt data portion
                        out_file.write(des.encrypt(chunk))

    elif mode == 'decrypt':
        # Initialise variables
        des = DES3.new(key, DES3.MODE_CFB, iv)
        in_filename = file_path
        out_filename = in_filename + ".decrypted"
        out_filename = str(out_filename).replace(".encrypted", "")
        # initialise the file to read
        with open(in_filename, 'r') as in_file:
            # initialise the file to write
            with open(out_filename, 'w') as out_file:
                while True:
                    chunk = in_file.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    # decrypt data portion
                    out_file.write(des.decrypt(chunk))

    else:
        print "main.py encrypt/decrypt file_path key"

if __name__ == '__main__':
    main()
