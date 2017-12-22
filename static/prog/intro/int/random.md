+++
title = "random"
subsections = ["intermediate"]
+++
This module allows you to create programs with randomness. This is
useful for many simple games.

First, import the module:

	>>> import random

Use `randint` to get random integers:

	>>> random.randint(1, 5)
	1
	>>> random.randint(1, 5)
	5
	>>> random.randint(1, 5)
	3

This will give us a random integer between 1 and 5.

{{% req "int/lists" %}}

If you have a list of cats and you want to pet a random cat, how could
you know which one to pet?

	>>> cats = ["foom", "spottie", "tiger"]

Recall that you can use integers to access the elements of the list:

	>>> cats[0]
	'foom'
	>>> cats[1]
	'spottie'
	>>> cats[2]
	'tiger'

What you need is a random integer between 0 and 2:

	>>> index = random.randint(0, 2)
	>>> cats[index]
	'foom'
	>>> index
	0
	>>> cats[random.randint(0, 2)]
	'foom'
	>>> cats[random.randint(0, 2)]
	'spottie'

Since you typically don't know the length of the list ahead of time,
you can use `len`:

	>>> cats[random.randint(0, len(cats))]
	'tiger'
	>>> cats.append('richard')
	>>> cats[random.randint(0, len(cats))]
	'foom'

But since this is such a common thing to do, the `choice` function will
handle it all for you:

	>>> random.choice(cats)
	'foom'
	>>> random.choice(cats)
	'tiger'
	>>> random.choice(cats)
	'richard'
