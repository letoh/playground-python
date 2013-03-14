#!/usr/bin/python

from functools import partial

class Compose(object):
    class __ComposeMeta(type):
        def __getattr__(s, name):
            obj = Compose()
            return getattr(obj, name)

    __metaclass__ = __ComposeMeta

    def __init__(s):
        s.top = None
        s.chain = None

    def __getattr__(s, name):
        new_fun = eval(name)
        if not callable(new_fun):
            raise TypeError("%s is not a callable" % name)
        if s.top is not None:
            if s.chain is None: s.chain = s.top
            else: s.chain = lambda x, f = s.top, g = s.chain: g(f(x))
        s.top = new_fun
        return s

    def __call__(s, *args, **kwargs):
        try: r = s.top(*args, **kwargs)
        except TypeError:
            s.top = partial(s.top, *args, **kwargs)
            return s
        return s.chain(r) if s.chain else r


if __name__ == '__main__':
    def foo(n, m): return n + m
    def bar(n, m): return n(m)

    a = Compose. foo(1) . bar(lambda x: x+2)
    print 'result:', a(3)
    print 'result:', a(4)
    
    from operator import eq, itemgetter
    eq0 = partial(eq, 0)
    fst = itemgetter(0)
    a = Compose. len . filter (eq0) . map (fst)
    print 'result:', a([(0, 2), (0, 4), (1, 3)])

    a = Compose. len . filter (eq0)
    b = Compose. map (fst)
    c = Compose. a . b
    print 'result:', c([(0, 2), (0, 4), (1, 3)])
