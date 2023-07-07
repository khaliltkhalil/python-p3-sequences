#!/usr/bin/env python3


def print_fibonacci(length):
    fibonacci = []

    for i in range(0, length):
        fibonacci.append(i if i < 2 else fibonacci[-1] + fibonacci[-2])

    print(fibonacci)
