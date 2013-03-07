#!/usr/bin/python

class Move:
	def __init__(s, f, t): s.f, s.t = f, t


def GetNextMove(n, f, t, m):
	if n == 1: yield Move(f, t)
	else:
		for M in GetNextMove(n - 1, f, m, t): yield M
		yield Move(f, t)
		for M in GetNextMove(n - 1, m, t, f): yield M


def main():
	for M in GetNextMove(3, 'A', 'B', 'C'): print M.f, '->', M.t


if __name__ == '__main__': main()

