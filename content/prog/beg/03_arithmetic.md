+++
title = "arithmetic"
date = "2016-12-28T03:15:42-07:04"
subsections = [ "beginner" ]
subsections_weight = 4
+++
You can use the Python interpreter like a calculator:

	>>> 2 + 2 - 1
	3
	>>> 7 * 3
	21
	>>> 20 / 5
	4.0
	>>> 2 ** 3
	8

(The `**` is for exponentiation). Notice that we didn't use `print`. In the interactive interpreter, typing something without `print` like this will display the value anyway. It's a shortcut so you don't have to type as much. In a normal program that you save in a file, you would have to write `print(2 + 2 - 1)`.

Be careful, because with great power comes great responsibility:

	>>> 666 / 0
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero
