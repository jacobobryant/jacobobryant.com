+++
title = "str and int"
subsections = ["core"]
subsections_weight = 60
+++
You can use variables to hold different types of data. You can store
numbers:

	>>> x = 42

You can also store text:

	>>> x = "hello there"

You have to be careful not to get these types mixed up. For instance,
this won't work:

	>>> x = 5
	>>> y = "4"
	>>> x + y
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'

What does `int` and `str` mean? `int` is short for integer. `5` is an
integer. `str` is short for string. A string is another word for text.
(Why do we call it a string instead of just text? I don't know.)
`"hello"` is a string.

More importantly, `"4"` is a string, not a number. You can't write `5
+ "4"` for the same reason that you can't write `5 + "bananas"`. This
is a problem when you need to get user input. The `input` function
returns a string, never a number. So this causes an error:

	>>> num = input("enter a number: ")
	enter a number: 5
	>>> print("666 plus", num, "is", 666 + num)
	Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' and 'str'

Never fear, the `int` function is here!

	>>> x = 5
	>>> y = "4"
	>>> x + int(y)
	9

`int` converts stuff into integers. We can use it to convert user
input to numbers:

	>>> print("666 plus", num, "is", 666 + int(num))
	666 plus 5 is 671

We can also do the conversion when we first get the number:

	>>> num = int(input("enter a number: "))
	enter a number: 7
	>>> print("666 plus", num, "is", 666 + num)
	666 plus 7 is 673
