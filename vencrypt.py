#!/usr/bin/python3

#Cynthia Zhu
#Professor Krzyzanowski
#Computer Security (01:198:419:02)
#April 12, 2022

#Project 3, Part 1/5
#Vigenère cipher encryption

#vencrypt.py key_file plaintext_file ciphertext_file

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
        with open(sys.argv[2], "rb") as plaintext_file:
            try:
                with open(sys.argv[3], "wb") as ciphertext_file:
                    i = 0
                    plaintext_byte = plaintext_file.read(1)
                    while plaintext_byte:
                        ciphertext_file.write(bytes([(plaintext_byte[0] + key[i % key_length]) % 256]))
                        i += 1
                        plaintext_byte = plaintext_file.read(1)
            except:
                print("Error: Ciphertext file error")
                sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except:
        print("Error: Plaintext file error")
        sys.exit(1)

if __name__ == "__main__":
    main()