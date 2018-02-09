+++
name = "if"
+++

What's the point of boolean values? So you can do things like this:

	>>> bufday_today = True
	>>> if bufday_today:
	        print("happy bufday!")
	    else:
	        print("go away")
	    
	happy bufday!

The two print statements are **indented**. Press Tab to indent those
lines.

The simplest `if` statement goes like this:

	>>> if True:
	        print("hello world!")
	    
	hello world!

The **body** of the `if` statement only executes if the expression
that comes after it is true.

	>>> if False:
	        print("hello world!")
	    
	>>>

You can have as many lines of code in the body as you like:

	>>> if True:
	        print("hello world!")
	        foo = 7 + 9
	        print(foo)
	    
	hello world!
	16

You can use `else` to execute code if the statement is false:

	>>> age = 15
	>>> if age >= 16:
	        print("you're old enough to drive.")
	    else:
	        print("go away")
	    
	go away

<!--
But what if you wanted more than two options? You could do this:

	>>> name = input("what is your name? ")
	what is your name? chuck norris
	>>> if name == "batman":
	        print("Welcome home, Bruce")  # spoiler alert
	    else:
	        if name == "chuck norris":
	            print("go away chuck")
	        else:
	            print("hello", name)
	   
	go away chuck

However, there's a simpler way to do it:

	>>> name = input("what is your name? ")
	what is your name? chuck norris
	>>> if name == "batman":
	        print("Welcome home, Bruce")
	    elif name == "chuck norris":
	        print("go away chuck")
	    else:
	        print("hello", name)
	   
	go away chuck

`elif` is short for "else if." You can add as many `elif`s as you
like:

	>>> temperature = 70
	>>> if temperature >= 212:
	        print("it's really hot")
	    elif temperature >= 100:
	        print("it's still really hot")
	    elif temperature >= 76:
	        print("it's uncomfortably hot")
	    elif temperature >= 68:
	        print("it's just right")
	    else:
	        print("BURMA SHAVE")
	    
	it's just right
-->


Now use an `if` statement to make `five.py` more interesting:

<pre>
>>> %Run five.py
Enter a number greater than five: <b>6</b>
good job
>>> %Run five.py
Enter a number greater than five: <b>4</b>
moron
</pre>

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# five.py
num = int(input("Enter a number greater than five: "))
if num > 5:
    print("good job")
else:
    print("moron")
```
</div>

{{% note %}}
This section is the first time you've seen indented code.
Whenever you see a `:` at the end of a line, it means one or more
lines following will be indented. We do this a lot to organize code.

The empty space that comes before each indented line is important.
Python uses it to know when a block of code ends. For example, notice
the difference between this:
	
	if 3 > 4:
	    print('abc')
	    print(123)
	print('wow')

and this:

	if 3 > 4:
	    print('abc')
	print(123)
	print('wow')

(If you don't see it, try running the code).
{{% /note %}}
