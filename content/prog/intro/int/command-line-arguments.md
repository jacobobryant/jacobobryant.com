+++
title = "command line arguments"
shorttitle = "CLI arguments"
subsections = ["intermediate"]
+++
{{% req "int/import" "int/lists" %}}
Remember `basic_io.py`? Here's how it works in case you've forgotton:

<pre>
$ <b>python basic_io.py</b>
What is your name? <b>kevin</b>
Go away kevin
</pre>

There's another way to pass data in to programs. We could write the
program so it works like this:

<pre>
$ <b>python basic_io.py kevin</b>
Go away kevin
</pre>

In the second example, we pass kevin in as an argument on the command
line. How does the program get access to kevin? Like so:

```python
# basic_io.py
import sys
print("Go away", sys.argv[1])
```

The `sys` package contains things that are related to the system. It
contains the `argv` variable (short for "argument vector"), which is a
list of command line arguments. Create the following file,
`arguments.py`:

```python
# arguments.py
import sys
print(sys.argv)
```

Now try running the program with different command line arguments. For
instance, here's some output I got:

<pre>
$ <b>python arguments.py foo bar baz</b>
['arguments.py', 'foo', 'bar', 'baz']
$ <b>python arguments.py hello my name is tom marvelo riddle</b>
['arguments.py', 'hello', 'my', 'name', 'is', 'tom', 'marvelo', 'riddle']
</pre>

Notice that spaces are used to separate command line arguments. We can
use quotes to include spaces inside the arguments:

<pre>
$ <b>python arguments.py hello my name is "tom marvelo riddle"</b>
['arguments.py', 'hello', 'my', 'name', 'is', 'tom marvelo riddle']
</pre>

The first element of argv is the name of the file, but we often don't
care about that. Change `arguments.py` so it looks like this:

```python
# arguments.py
import sys
print(sys.argv[1:])
```

Now you'll get output like this:

<pre>
$ <b>python arguments.py id like to be</b>
['id', 'like', 'to', 'be']
$ <b>python arguments.py under the sea</b>
['under', 'the', 'sea']
$ <b>python arguments.py in an octopuses garden</b>
['in', 'an', 'octopuses', 'garden']
$ <b>python arguments.py in the shade</b>
['in', 'the', 'shade']
</pre>
