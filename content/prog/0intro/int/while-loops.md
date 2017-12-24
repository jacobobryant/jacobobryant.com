+++
title = "while loops"
subsections = ["intermediate"]
+++

When getting user input, sometimes they type the wrong stuff:

	>>> response = input("Would you like fries with that? (yes/no) ")
	Would you like fries with that? boleh
	>>> response
	'boleh'

This response would be ok if you happen to speak Malay, but since you
probably don't, it's not. We'd like a yes or no response. You could
check the user's input like this:

	>>> if response == "yes":
	...     print("have some fries")
	... elif response == "no":
	...     print("fine, I'll eat them myself")
	... else:
	...     print("invalid input")
	...     response = input("Would you like fries with that? (yes/no) ")
	... 
	invalid input
	Would you like fries with that? (yes/no) no
	>>> 

This works if the user types the right thing on the second try. That
however is a bad expectation to have. It's especially bad if you're
writing software for an infinite number of [monkeys](https://en.wikipedia.org/wiki/Infinite_monkey_theorem).
We'd like to keep asking the user for input until they do
it right. We can do it like so:

	>>> response = ""
	>>> while response != "yes" and response != "no":
	...     response = input("Would you like fries with that? (yes/no) ")
	... 
	Would you like fries with that? (yes/no) boleh
	Would you like fries with that? (yes/no) hohoho
	Would you like fries with that? (yes/no) burma shave
	Would you like fries with that? (yes/no) to be or not to be
	Would you like fries with that? (yes/no) yes
	>>> 

This is a `while` loop. After the `while` keyword, you type a boolean
expression. If the expression is true, the body of the while loop will
be executed (just like in an `if` statement). But then the while loop
will check the expression again. It will keep executing the body over
and over again until the expression becomes false.

See if you can write a program that does the following:

	$ python number.py
	Enter a number between 1 and 10: 0
	Enter a number between 1 and 10: 11
	Enter a number between 1 and 10: 666
	Enter a number between 1 and 10: 5
	Good job. Your number: 5

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# number.py
number = 0
while number < 1 or number > 10:
    number = int(input("Enter a number between 1 and 10: "))
print("Good job. Your number:", number)
```
