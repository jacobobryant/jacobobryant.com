+++
name = "arithmetic"
+++
You can use the Python interpreter like a calculator:

	>>> print(2 + 2 - 1)
	3
	>>> print(7 * 3)
	21

The Python interpreter has a shortcut so you don't have to use
`print`:

	>>> 20 / 5
	4.0
	>>> 2 ** 3
	8

Be careful, because with great power comes great responsibility:

	>>> 666 / 0
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero
