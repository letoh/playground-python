#!/usr/bin/python

def fact(n, k = lambda x: x):
	if n == 0: return k(1)
	return fact(n - 1, lambda x: k(n * x))

for n in xrange(10):
	print n, fact(n)

def fact(n, a = 1, k = lambda x: x):
	if n == 0: return k(a)
	return fact(n - 1, n * a, k)

for n in xrange(10):
	print n, fact(n)

