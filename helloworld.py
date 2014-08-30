#!python2

def f():
	a = 'hello world!'

	print(a)
	print('i am the king!!!')
	max(44, 88)

def max(a, b):
	if a > b:
		print(a)
	else:
		print(b)

d = max(33, 44)
print(d)
f()

def max2(a, b):
	if a > b:
		return a
	else:
		return b

c = max2(55, 66)
print(c)
