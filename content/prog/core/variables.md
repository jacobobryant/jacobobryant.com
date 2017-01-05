+++
title = "variables"
date = "2016-12-28T03:15:42-07:01"
subsections = [ "core" ]
subsections_weight = 1
+++
To store data for later use, we use variables:

	>>> x = 666
	>>> print(x)
	666
	>>> my_name = "jacob"
	>>> print(my_name)
	jacob
	>>> my_name = x
	>>> print(my_name)
	666

The variable is created when you first assign a value to it with the `=` operator. Trying to use a variable before creating it will make your program crash:

	>>> print(bar)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'bar' is not defined
	>>> bar = 666
	>>> print(bar)
	666
