#!/usr/bin/python3

#Cynthia Zhu
#Professor Krzyzanowski
#Computer Security (01:198:419:02)
#April 12, 2022

#Project 3, Part 2/5
#Vigenère cipher decryption

#vdecrypt.py key_file ciphertext_file plaintext_file

import sys

def main():
    if len(sys.argv) < 4:
        print("Error: Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("Error: Too many arguments")
        sys.exit(1)
    key = bytearray()
    key_length = len(key)
    try:
        with open(sys.argv[1], "rb") as key_file:
            key_byte = key_file.read(1)
            if key_byte:
                while key_byte:
                    key.extend(key_byte)
                    key_byte = key_file.read(1)
                key = list(key)
                key_length = len(key)
            else:
                print("Error: Empty key file")
                sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except:
        print("Error: Key file error")
        sys.exit(1)
    
    try:
        with open(sys.argv[2], "rb") as ciphertext_file:
            try:
                with open(sys.argv[3], "wb") as plaintext_file:
                    i = 0
                    ciphertext_byte = ciphertext_file.read(1)
                    while ciphertext_byte:
                        plaintext_file.write(bytes([(ciphertext_byte[0] - key[i % key_length] + 256) % 256]))
                        i += 1
                        ciphertext_byte = ciphertext_file.read(1)
            except:
                print("Error: Plaintext file error")
                sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except:
        print("Error: Ciphertext file error")
        sys.exit(1)

if __name__ == "__main__":
    main()