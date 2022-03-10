import time
from hashlib import sha256
from os import urandom
from random import random, getrandbits, randint

TRUNCATED_BOUND = [x for x in range(8, 50, 2)]
MODIFY_BIT = 7

def main():
    task_one()

"""
Task One

find a collision using strings with hamming distance of one and 
a truncated sha256 hash
"""
def task_one():
    for size in TRUNCATED_BOUND:
        match = False
        attempts = 0
        start = time.time()
        while not match:
            a, b = generate_hamming_strings(size)
            hash_a = trunc_hash(a, size)
            hash_b = trunc_hash(b, size)
            match = (hash_a == hash_b)
            attempts += 1

        end = time.time()
        print(f"{size}-bit hash strings match...\n{hash_a}\n{hash_b}")
        print(f"Time elapsed: {end - start} with {attempts} attempts.")


# TODO: make function that generates sha256 hash from arbitary input
def my_hash(x):
    x = str(x).encode()
    return sha256(x).digest().hex()

# TODO: truncate the results of the hash function in order to find collisions
def trunc_hash(x, size):
    result = my_hash(x)
    int_rep = int(result, 16)
    binary_rep = bin(int_rep)[:size]
    int_rep = int(binary_rep, 2)
    hex_rep = hex(int_rep)
    return hex_rep


def generate_hamming_strings(size):
    og = getrandbits(size)
    modify_bit = randint(0, size)
    new = og ^ (1 << modify_bit)

    return og, new



if __name__ == '__main__':
    main()
