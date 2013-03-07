#!/usr/bin/python

def sum(lst):
    def sum0(lst, ans):
        if not lst: return ans
        return sum0(lst[1:], ans + lst[0])
    return sum0(lst, 0)

print sum([3,3,2,2,1])


# Y(F) = F(Y(F))
#      = F(F(Y(F)))

def Y(F):
    #return F(Y(F))
    return F(lambda x: (Y(F))(x))

Y = lambda F: \
    (lambda x: F(lambda y: (x(x))(y))) \
    (lambda x: F(lambda y: (x(x))(y)))

FactGen = lambda f: lambda n: n == 0 and 1 or (n * f(n-1))
print (Y(FactGen))(6)

SumGen = lambda s: lambda l: 0 if not l else l[0] + s(l[1:])
print (Y(SumGen))([1,2,3,4,5])

FibGen = lambda g: lambda n: 1 if (n <= 1) else g(n-1) + g(n-2)
print (Y(FibGen))(5)


sum = \
    (lambda x: lambda lst: 0 if not lst else lst[0] + x(x)(lst[1:])) \
    (lambda x: lambda lst: 0 if not lst else lst[0] + x(x)(lst[1:]))

print sum([1,2,3,4,5,6,7])

