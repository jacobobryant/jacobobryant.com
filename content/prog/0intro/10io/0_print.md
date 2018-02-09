+++
name = "print"
+++
<!--
{{% note "course organization" %}}
The best way to learn programming is to first think of a program and then
figure out how to create it. This course will help you learn in this way.
However, there are a few core tools that will be used in nearly all the
programs you write. This section will teach you those tools. 
{{% /note %}}
-->

There are many commands available to you in Python. These commands are called
**functions**. The `print` function displays a message to the user (it "prints"
the message to your screen). As you've seen, you can use it like this:

	>>> print("hello world")
	hello world

Using a function like this is called **calling** a function. You call a function
by adding parentheses at the end. You can give information to the function by
putting things inside the parentheses. Each piece of information we give to the
function is called an **argument**. Above, we passed only one argument (a line of
text) to `print`.

When you pass text as an argument,
make sure you put quotes around the words. If you
don't, you'll get an error. You don't need to put quotes around
numbers, though.

	>>> print(hello)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'hello' is not defined
	>>> print("hello")
	hello
	>>> print(3)
	3

You can use either double or single quotes; it doesn't matter:

	>>> print("hello there")
	hello there
	>>> print('hello there')
	hello there

We can pass multiple arguments to a function by separating
the arguments with commas, like this:

	>>> print("one", 2, "three")
	one 2 three

{{% tip %}}
When you see Python shell examples like the ones above, try typing similar
commands on your own. Often, things will not make sense until you do it
yourself.
{{% /tip %}}

