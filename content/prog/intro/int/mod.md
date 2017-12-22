+++
title = "mod"
subsections = ["intermediate"]
+++

Say hello to the `%` operator (pronounced "the mod operator"):

	>>> 20 % 3
	2
	>>> 15 % 5
	0
	>>> def foo(a, b):
	...     print(a, "divided by", b, "is", int(a / b),
	...           "with a remainder of", a % b)
	... 
	>>> foo(20, 3)
	20 divided by 3 is 6 with a remainder of 2
	>>> foo(15, 5)
	15 divided by 5 is 3 with a remainder of 0
	>>> foo(666, 7)
	666 divided by 7 is 95 with a remainder of 1

You can use the mod operator to find out if a number is even:

	>>> def bar(n):
	...     if n % 2 == 0:
	...             print(n, "is even")
	...     else:
	...             print(n, "is odd")
	... 
	>>> bar(1)
	1 is odd
	>>> bar(2)
	2 is even
	>>> bar(1234)
	1234 is even
