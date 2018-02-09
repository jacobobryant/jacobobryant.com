+++
name = "booleans"
+++
You already know that variables can hold numbers and strings. They can
also hold a third type of data: **booleans**.

	>>> foo = True
	>>> print(foo)
	True
	>>> foo = False
	>>> print(foo)
	False

"Boolean" values are just true/false values. They're named after
[George Boole](https://en.wikipedia.org/wiki/George_Boole), a guy who
did a lot of fancy stuff with true/false values.

You can use **comparison operators** to create **expressions** that
evaluate to booleans:

	>>> print(4 < 5)
	True
	>>> 10 > 11
	False
	>>> 7 == 7
	True
	>>> 14 >= 5
	True
	>>> 9 <= 9
	True

Note that we wrote `7 == 7` instead of `7 = 7`. That's because we use
a single `=` for assigning values to variables, as in `foo = 7`. We
call it the **assignment operator**. The
double `==` is a comparison operator. It compares two things and
checks if they're equal.

Just like with arithmetic operators, you can store the results of expressions in variables:

	>>> foo = 5 * 3
	>>> foo
	15
	>>> bar = 5 < 3
	>>> bar
	False
	>>> baz = 14 == 14
	>>> baz
	True

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

Remember to use `int` to convert the user input to an actual number.

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# five.py
num = int(input("Enter a number greater than five: "))
print(num > 5)
```
</div>

Now make the following program:
<pre>
>>> %Run five.py
Enter a number: <b>4</b>
Enter another number: <b>5</b>
4 is less than 5: True
4 is equal to 5: False
4 is greater than 5: False
</pre>
