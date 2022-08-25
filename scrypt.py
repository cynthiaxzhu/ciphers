#!/usr/bin/python3

#Cynthia Zhu
#Professor Krzyzanowski
#Computer Security (01:198:419:02)
#April 12, 2022

#Project 3, Part 3/5
#stream cipher encryption, decryption

#scrypt.py password plaintext_file ciphertext_file
#scrypt.py password ciphertext_file plaintext_file

import sys

#linear congruential generator
def lcg(x):
    return ((1103515245 * x) + 12345) % 256

#small database manager
def sdbm(s):
    hash = 0
    for c in s:
        hash = ord(c) + (hash << 6) + (hash << 16) - hash
    return hash

def main():
    if len(sys.argv) < 4:
        print("Error: Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("Error: Too many arguments")
        sys.exit(1)
    try:
        with open(sys.argv[2], "rb") as input_file:
            try:
                with open(sys.argv[3], "wb") as output_file:
                    password = sys.argv[1]
                    seed = sdbm(password)
                    key_byte = lcg(seed)
                    input_byte = input_file.read(1)
                    while input_byte:
                        output_file.write(bytes([input_byte[0] ^ key_byte]))
                        key_byte = lcg(key_byte)
                        input_byte = input_file.read(1)
            except:
                print("Error: Output file error")
                sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except:
        print("Error: Input file error")
        sys.exit(1)

if __name__ == "__main__":
    main()