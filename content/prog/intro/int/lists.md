+++
title = "lists"
subsections = ["intermediate"]
+++
Use lists to store multiple values in a single variable.

	>>> mylist = ["hello", 4, "ho ho ho", "so it has come to this"]

Each "element" of the list can be accessed by providing an "index" inside of brackets:

	>>> mylist[0]
	'hello'
	>>> mylist[1]
	4
	>>> mylist[2]
	'ho ho ho'
	>>> mylist[3]
	'so it has come to this'


Notice that the first element has an index of 0, not 1.

You can change individual elements:

	>>> print(mylist)
	['hello', 4, 'ho ho ho', 'so it has come to this']
	>>> mylist[2] = 'i like cheese'
	>>> print(mylist)
	['hello', 4, 'i like cheese', 'so it has come to this']

You can add more elements with `append`:

	>>> mylist.append(42)
	>>> mylist
	['hello', 4, 'i like cheese', 'so it has come to this', 42]

`len` will tell you how many elements there are:

	>>> len(mylist)
	5

`pop` will remove the element at the given index:

	>>> mylist.pop(0)
	'hello'
	>>> mylist
	[4, 'i like cheese', 'so it has come to this', 42]
	>>> mylist.pop(2)
	'so it has come to this'
	>>> mylist
	[4, 'i like cheese', 42]

You can get a "sub-list" by using a colon inside of the brackets:

	>>> mylist = ['a', 'b', 'c', 'd', 'e']
	>>> sublist = mylist[1:3]
	>>> sublist
	['b', 'c']

The first number (1) is the index of the first element we want ("b"). The
second number (3) is the index of the element right *after* the last element we
want ("c").

You can leave out the first number to start from the first element:

	>>> mylist[:3]
	['a', 'b', 'c']

And you can leave out the second number to end at the last element:

	>>> mylist[1:]
	['b', 'c', 'd', 'e']
