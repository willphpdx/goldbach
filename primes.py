#!/usr/bin/env python3
# credit: @epitron for the generators (https://gist.github.com/epitron)

from itertools import islice
from time import time

def time_generator(func, n=100):
  generator = func()
  start     = time()
  islice(generator, n)
  elapsed   = time() - start

  print("[%s] %0.9fs (%d iterations): " % (func.__name__, elapsed, n))

def prime_generator_pseudotest():
  """ A pseudo-prime testing trick in a generator expression """
  small_primes = (2, 3, 5, 7, 11)
  p = 2
  while True:
    if 0 not in (pow(w,p-1,p)==1 for w in small_primes if p > w):
      yield p
    p += 1


def prime_generator():
  """ Yields the sequence of prime numbers via the Sieve of Eratosthenes. """
  D = {}  # map composite integers to primes witnessing their compositeness
  q = 2   # first integer to test for primality
  while 1:
    if q not in D:
      yield q        # not marked composite, must be prime]
      D[q*q] = [q]   # first multiple of q not already marked

    else:
      for p in D[q]: # move each witness to its next multiple
        D.setdefault(p+q,[]).append(p)
      del D[q]       # no longer need D[q], free memory

    q += 1

time_generator(prime_generator)
time_generator(prime_generator_pseudotest)

start = time()
P = {}
PP = {}
pg = prime_generator()
P[0] = next(pg)
for i in range(1, 1000000):
    p = next(pg)
    P[i] = p

    for j in range(i-1):
        bin = P[j]+p
        if bin in PP:
            PP[bin] += 1
        else:
            PP[bin] = 1
    if(i%100 == 0):
        print(int(time() - start), i, p)


print(PP)
print(time() - start)
