+++
name = "variables"
+++
To store data for later use, we use variables:

	>>> x = 666
	>>> print(x)
	666
	>>> my_name = "jacob"
	>>> print("hello", my_name)
	hello jacob
	>>> my_name = x
	>>> print(my_name, 7)
	666 7

The variable is created when you first assign a value to it with the `=` operator. Trying to use a variable before creating it will make your program crash:

	>>> print(bar)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'bar' is not defined
	>>> bar = 666
	>>> print(bar)
	666

Take a second to appreciate the difference between these two calls to
print:

	>>> foo = "bar"
	>>> print("foo")
	foo
	>>> print(foo)
	bar
