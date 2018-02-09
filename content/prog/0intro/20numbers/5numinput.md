+++
name = "number input"
+++
Now what if you want to do some math with user-inputted numbers?

<pre>
>>> %Run dog.py
Enter your age: <b>23</b>
You are 3.2857142857142856 in dog years.
</pre>

How would you write that program? You might try something like this:

```python
age = input("Enter your age: ")
dog_years = age / 7
print("You are", dog_years, "in dog years.")
```

Copy and paste that code into Thonny and see what happens if you try
to run it.

Surprise, it doesn't work. That's because `age` is a **string**. (In
programming, a string is a piece of text). Anything you get from
`input` will always be a string. So if the user types `23` in our
program above, the middle line is effectively doing this:

```python
dog_years = "23" / 7
```

It still makes sense to you, but to the computer, this is as
nonsensical as trying to say `dog_years = "hohoho" / 7`. You can't do
normal arithmetic with strings. You can solve this problem with `int`:

```python
age = input("Enter your age: ")
age_as_a_number = int(age)
dog_years = age_as_a_number / 7
print("You are", dog_years, "in dog years.")
```

`int` is short for integer, which basically means a whole number. It
tries to turn whatever you give it into an integer. To make the
program shorter, you could also write it like this:

```python
age = int(input("Enter your age: "))
dog_years = age / 7
print("You are", dog_years, "in dog years.")
```

If `int` doesn't know how to convert whatever you gave it into an
integer, it'll crash:

	>>> int("7")
	7
	>>> int("-38")
	-38
	>>> int("aoeu")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: 'aoeu'
	>>> int("7.5")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '7.5'

(Even though 7.5 is a number, it's not an integer, so `int` fails).
