+++
title = "list comprehensions"
subsections = ["intermediate"]
+++
{{% req "int/lists" "int/for-loops" %}}

Consider the following list:

	>>> numbers = [3, 42, 666]

What if you want to add 7 to each element of the list? You could do it
like this:

	>>> numbers[0] = numbers[0] + 7
	>>> numbers[1] = numbers[1] + 7
	>>> numbers[2] = numbers[2] + 7
	>>> numbers
	[10, 49, 673]

But since you know about for loops, you can instead create a new list
like this:

	>>> numbers = [3, 42, 666]
	>>> new_numbers = []
	>>> for n in numbers:
	...     new_numbers.append(n + 7)
	... 
	>>> new_numbers
	[10, 49, 673]

This sort of thing is so common that there's a short hand way of doing
it:

	>>> new_numbers = [n + 7 for n in numbers]
	>>> new_numbers
	[10, 49, 673]

The `[n + 7 for n in numbers]` part is called a list comprehension.
Python programmers use them all the time.
