+++
title = "booleans"
subsections = [ "core" ]
subsections_weight = 80
+++
There's another type of data you can store in variables: **booleans**.

	>>> foo = True
	>>> foo
	True
	>>> foo = False
	>>> foo
	False

"Boolean" values are just true/false values. They're named after
[George Boole](https://en.wikipedia.org/wiki/George_Boole), a guy who
did a lot of fancy stuff with true/false values.

You can use **comparison operators** to create expressions that
evaluate to booleans:

	>>> print(4 < 5)
	True
	>>> 10 > 11
	False
	>>> 7 == 7
	True

Note that we write `7 == 7` instead of `7 = 7`. That's because we use
a single `=` for assigning values to variables, as in `foo = 7`. We
call it the **assignment operator**. The
double `==` is a comparison operator. It compares two things and
checks if they're equal.

Now write a program called `five.py` that tells you if the number you
entered is greater than five:

<pre>
>>> %Run five.py
Enter a number greater than five: <b>4</b>
False
>>> %Run five.py
Enter a number greater than five: <b>5</b>
False
>>> %Run five.py
Enter a number greater than five: <b>34</b>
True
</pre>

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# five.py
num = int(input("Enter a number greater than five: "))
print(num > 5)
```
</div>
