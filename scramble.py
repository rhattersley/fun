#!/usr/bin/python3
import random
import sys


A2Z = 'abcdefghijklmnopqrstuvwxyz'


def random_key():
    key = list(A2Z)
    random.shuffle(key)
    key = ''.join(key)
    return key


def scramble(src_path):
    with open(src_path) as src:
        lines = src.readlines()
    key = random_key()
    with open("key.txt", "w") as f:
        print(key, file=f)
    table = str.maketrans(A2Z + A2Z.upper(), key + key.upper())
    for line in lines:
        print(line.strip().translate(table))


if __name__ == "__main__":
    _, src_path = sys.argv
    scramble(src_path)
