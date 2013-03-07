#!/usr/bin/python

import ctypes
from ctypes import CDLL, c_void_p, c_int, Structure, addressof
from ctypes.util import find_library

libc = CDLL(find_library('c'))

addr = ctypes.cast(libc.printf, c_void_p).value
print "addr =", hex(addr)

#
# a.c: gcc -o liba.so -shared a.c
#
# typedef int (*p)(const char*, ...);
#
# int go(int addr)
# {
#     p f = (p)addr;
#     printf("1 call addr %p from %s\n", f, __func__);
#     return f("2 call addr %p from %s\n", f, __func__);
# }
#

liba = CDLL("./liba.so")
liba.go(c_int(addr))

