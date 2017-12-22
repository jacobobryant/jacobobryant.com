+++
title = "for loops"
subsections = ["intermediate"]
+++
{{% req "int/lists" %}}

Suppose you created a list to store the names of your cats:

	>>> cats = ["foom", "spottie", "salt", "pete"]

What if you wanted to greet each cat? You could do it like this:

	>>> print("hello", cats[0])
	hello foom
	>>> print("hello", cats[1])
	hello spottie
	>>> print("hello", cats[2])
	hello salt
	>>> print("hello", cats[3])
	hello pete

However, that would get tedious if you have a lot of cats. There's a better
way:

	>>> for cat in cats:
	...     print("hello", cat)
	... 
	hello foom
	hello spottie
	hello salt
	hello pete

This is called a "for loop". It's basically the same as doing this:

```python
cat = cats[0]
print("hello", cat)

cat = cats[1]
print("hello", cat)

cat = cats[2]
print("hello", cat)

cat = cats[3]
print("hello", cat)
```

But with a for loop, you don't have to worry about how many elements are in the
list. `for` will go through each element automatically (and you don't have to
type as much with a for loop).

You can loop through a list without first assigning the list to a variable:

	>>> for x in [1, 2, 3]:
	...     print(x)
	... 
	1
	2
	3

You can include more than one line in the body of the for loop:

	>>> for x in [1, 2, 3]:
	...     x_squared = x ** 2
	...     print(x, "squared is", x_squared)
	... 
	1 squared is 1
	2 squared is 4
	3 squared is 9
