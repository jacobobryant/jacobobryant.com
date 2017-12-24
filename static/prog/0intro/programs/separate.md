+++
title = "separate"
subsections = [ "programs" ]
subsections_weight = 0
draft = true
+++

The time has come to separate even numbers from odd. You must write a
program `separate.py` that will take a list of integers as command line arguments,
and then it will print out first a sorted list of the even numbers and second
a sorted list of the odd numbers. For example:

<pre>
$ <b>python hw6.py 1 3 482 394 10 29</b>
[10, 394, 482]
[1, 3, 29]
$ <b>python hw6.py 7 13 42 101 5 666 0</b>
[0, 42, 666]
[5, 7, 13, 101]
</pre>

{{% req "int/lists"
	"int/for-loops"
	"int/command-line-arguments"
	"int/mod"
	"int/sorted" %}}

In English, try to write down a step-by-step procedure for how this
program will work. You should have roughly one step for each line.
After you've given it your best shot, take a look at the algorithm I
came up with.

<a href="#algorithm" class="btn btn-info" data-toggle="collapse">Show algorithm</a>
<div id="algorithm" class="collapse">

1. Make two empty lists, one for even numbers and one for odd numbers.
2. For each command line argument:
	1. Convert the argument from a string to an integer
	2. If the number is even, add it to the list of even numbers
	3. Otherwise, add it to the list of odd numbers
3. Sort and print both lists

</div>

Now that you've got the algorithm figured out, try to write out the
code. Take a look at my code if you get stuck.

<a href="#code" class="btn btn-info" data-toggle="collapse">Show code</a>
<div id="code" class="collapse">
```python
# separate.py
import sys
evens = []
odds = []
for arg in sys.argv[1:]:
    n = int(arg)
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print(sorted(evens))
print(sorted(odds))
```
</div>
