+++
title = "sorted"
subsections = ["intermediate"]
+++
{{% req "int/lists" %}}

Sometimes you just want to sort something.

	>>> words = ['go', 'hang', 'a', 'salami', 'im', 'a', 'lasagna', 'hog']
	>>> sorted_words = sorted(words)
	>>> print(sorted_words)
	['a', 'a', 'go', 'hang', 'hog', 'im', 'lasagna', 'salami']
	>>> numbers = [3, -2, 0, 666, 38, 42] 
	>>> sorted(numbers)
	[-2, 0, 3, 38, 42, 666]

Ta-da.
