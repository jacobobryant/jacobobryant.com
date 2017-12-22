+++
title = "enumerate"
subsections = ["intermediate"]
draft = true
+++
{{< req "int/for-loops"
			  "int/multiple-assignment" >}}
Let us once again consider the felines, how they toil not, neither do they
spin:

	>>> cats = ["foom", "spottie", "salt", "pete"]

What if you wanted to assign each of your kitties a number? You could do this:

	>>> i = 0
	>>> for cat in cats:
	...     print("cat number", i, "is", cat)
	...     i += 1
	... 
	cat number 0 is foom
	cat number 1 is spottie
	cat number 2 is salt
	cat number 3 is pete

`enumerate` is a function that lets you do this with less typing.

	>>> list(enumerate(cats))
	[(0, 'foom'), (1, 'spottie'), (2, 'salt'), (3, 'pete')]
