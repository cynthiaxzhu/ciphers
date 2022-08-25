#!/usr/bin/python3

#Cynthia Zhu
#Professor Krzyzanowski
#Computer Security (01:198:419:02)
#April 12, 2022

#Project 3, Part 4/5
#block cipher encryption

#sbencrypt.py password plaintext_file ciphertext_file

import sys

BLOCK_SIZE = 16

#linear congruential generator
def lcg(x):
    return ((1103515245 * x) + 12345) % 256

#small database manager
def sdbm(s):
    hash = 0
    for c in s:
        hash = ord(c) + (hash << 6) + (hash << 16) - hash
    return hash

def get_key_block(x):
    key_block = [lcg(x)]
    for i in range(1, BLOCK_SIZE):
        key_block.append(lcg(key_block[i - 1]))
    return key_block

def pad(plaintext_block):
    n = BLOCK_SIZE - len(plaintext_block)
    for _ in range(n):
        plaintext_block.append(n)
    return plaintext_block

def xor(block_1, block_2):
    return [b1 ^ b2 for (b1, b2) in zip(block_1, block_2)]

def shuffle(temp_block, key_block):
    for key in key_block:
        first = (key >> 4) & 0xF
        last = key & 0xF
        temp_block[first], temp_block[last] = temp_block[last], temp_block[first]
    return temp_block

def main():
    if len(sys.argv) < 4:
        print("Error: Too few arguments")
        sys.exit(1)
    if len(sys.argv) > 4:
        print("Error: Too many arguments")
        sys.exit(1)
    try:
        with open(sys.argv[2], "rb") as plaintext_file:
            try:
                with open(sys.argv[3], "wb") as ciphertext_file:
                    password = sys.argv[1]
                    seed = sdbm(password)
                    key_block = get_key_block(seed)
                    
                    previous_ciphertext_block = key_block
                    plaintext_block = plaintext_file.read(BLOCK_SIZE)
                    run = True
                    
                    while run:
                        plaintext_block = list(plaintext_block) if plaintext_block else list()
                        if len(plaintext_block) < BLOCK_SIZE:
                            run = False
                            plaintext_block = pad(plaintext_block) #1
                        temp_block = xor(plaintext_block, previous_ciphertext_block) #2
                        key_block = get_key_block(key_block[-1]) #3
                        temp_block = shuffle(temp_block, key_block) #4
                        ciphertext_block = xor(temp_block, key_block) #5
                        
                        ciphertext_file.write(bytes(ciphertext_block))
                        
                        previous_ciphertext_block = ciphertext_block
                        plaintext_block = plaintext_file.read(BLOCK_SIZE)
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