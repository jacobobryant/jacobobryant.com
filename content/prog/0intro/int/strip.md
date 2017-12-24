+++
title = "strip"
subsections = ["intermediate"]
+++
Suppose you use `input` to get some data from the user:

	>>> name = input('what is your name? ')
	what is your name? kevin
	>>> print("hello", name, "how are you?")
	hello kevin how are you?

What happens if kevin accidentally adds some spaces when he types his name?

	>>> name = input('what is your name? ')
	what is your name?        kevin    
	>>> print("hello", name, "how are you?")
	hello        kevin how are you?

When getting user input, we often would like to get rid of any whitespace on the ends.
`strip` will do just that:

	>>> name = '  kevin\n  '
	>>> name.strip()
	'kevin'
	>>> name
	'  kevin\n  '
