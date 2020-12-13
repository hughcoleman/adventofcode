#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import functools

def _gcd(a, b):
    """ Find the Greatest Common Divisor of two integers a and b. """
    return math.gcd(a, b)

def _lcm(a, b):
    """ Find the Lowest Common Multiple of two integers a and b. """
    return abs(a*b) // math.gcd(a, b)

def gcd(ns):
    """ Find the Greatest Common Divisor of a list of integers ns. """
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        while b:
            a, b = b, a%b
        ns.append(a)
    return ns[0]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def lcm(ns):
    """ Find the Lowest Common Multiple of a list of integers ns. """
    while len(ns) > 1:
        a, b = ns.pop(), ns.pop()
        ns.append(_lcm(a, b))
    return ns[0]

def modinv(a, m):
    """ Compute the modular multiplicative inverse of a mod m. """
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception(f"modular inverse of {a} (mod {m}) does not exist")
    else:
        return x % m

def crt(n, m):
    """ The Chinese Remainder Theorem. """
    sum_ = 0
    product = functools.reduce(lambda p, q: p*q, n)
    for n_i, m_i in zip(n, m):
        p = product // n_i
        sum_ += m_i * modinv(p, n_i) * p
    return sum_ % product

def factor(n):
    """ Compute the prime factors of n. """
    factors = {}
    i = 2
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n = n // i
            if i not in factors.keys():
                factors[i] = 0
            factors[i] = factors[i] + 1

    if n > 1:
        if n not in factors.keys():
            factors[n] = 0
        factors[n] = factors[n] + 1
    
    return factors

# Common number set membership lambdas.
triangular = lambda n: n in [0, 1] or any(i*(i+1)/2 == n for i in range(n))
fibonacci  = lambda n: square(5*n*n + 4) or square(5*n*n - 4)
square     = lambda n: int(math.sqrt(n))**2 == n
sphenic    = lambda n: list(factor(n).values()) == [1, 1, 1]
achilles   = lambda n: n >= 2 and all(e >= 2 for e in factor(n).values()) and \
                       gcd(list(factor(n).values())) == 1
prime      = lambda n: n not in [0, 1] and all(n % i > 0 for i in range(2, n-1))
emirp      = lambda n: prime(n) and prime(int(str(n)[::-1]))