#!/usr/bin/python
"""
monad test
"""

def _return(v):
	return lambda : v

#def _bind(a, f):
#	return f(a)

def _bind(a, f):
	v = a
	if callable(a):
		v = a()
	if v is None:
		return _return(None)
	return f(v)

# use function

def f_inc(v):
	return _return(int(v).__add__(1))

print _bind(_bind(_return(5), f_inc), f_inc)()

# use monad

def m_inc(a):
	return _bind(a, lambda v: _return(int(v).__add__(1)))

print m_inc(m_inc(_return(5)))()

def m_add(a, n):
	return _bind(a, lambda v: _return(int(v).__add__(n)))

print m_inc(m_inc(m_add(_return(5), 5)))()

def m_div(a, n):
	if not n:
		return _return(None)
	return _bind(a, lambda v: _return(int(v).__div__(n)))

print m_inc(m_inc(m_div(m_add(_return(5), 5), 2)))()
print m_inc(m_inc(m_div(m_add(_return(5), 5), 0)))()


#
# manage state
#

def _return(v):
	return lambda s: (v, s)

def _bind(a, f):
	def _bind_impl(s):
		v, sn = a, s
		if callable(a):
			v, sn = a(s)
		return f(v)(sn)
	return _bind_impl

# need pass a initial state
print '-' * 40
print m_inc(m_inc(m_div(m_add(_return(5), 5), 2)))(0)


def _set_value(v):
	return lambda s: (v, v)

def m_set_state(a):
	return _bind(a, lambda v: _set_value(v))

print m_inc(m_inc(m_set_state(m_add(_return(5), 5))))(0)

def _get_state():
	return lambda s: (s, s)

def m_add_from_state(a):
	#return _bind(a, lambda v: lambda s: (int(v).__add__(s), s))
	return _bind(a, lambda v: _bind(_get_state(), lambda s: _return(int(v).__add__(s))))

print m_inc(m_add_from_state(m_inc(m_set_state(m_add(_return(5), 5)))))(0)


def m_count():
	return _bind(_get_state(), lambda s: _set_value(int(s).__add__(1)))

def m_inc(a):
	return _bind(a, lambda v:
			     _bind(m_count(), lambda _:
					   _return(int(v).__add__(1))))

print m_inc(m_inc(m_add(_return(5), 5)))(0)


#
# identity monad
#
def _return(v):
	return lambda : v

def _bind(a, f):
	return f(a())

def m_identity(a):
	return _bind(a, lambda v: _return(v))

print m_identity(_return(5))()


#
# monad laws
#
def left_ientity():
	f = lambda v: v + 1
	assert(_bind(_return(5), f) == f(5))

left_ientity()

def right_identity():
	m_e = _return(5)
	#assert(_bind(m_e, _return) is m_e)
	assert(_bind(m_e, _return)() == m_e())

right_identity()

def associativity():
	m_e = _return(5)
	#assert(_bind(_bind(m_e, _return), _return) == _bind(m_e, lambda v: _bind(_return(v), _return)))
	assert(_bind(_bind(m_e, _return), _return)() == _bind(m_e, lambda v: _bind(_return(v), _return))())

associativity()

