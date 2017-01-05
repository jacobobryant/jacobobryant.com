+++
title = "basic io"
date = "2016-12-28T03:15:42-07:03"
subsections = [ "core" ]
subsections_weight = 3
+++
{{% note %}}
This section requires you to write your Python commands in a text file instead
of typing them into the Python shell. You'll need a good text editor for that. If you're
on Windows, the default text editor is Notepad,  a terrible editor. Instead, I recommend
[Notepad++](https://notepad-plus-plus.org/download/). If you're on Linux or OS
X, whatever the default is will probably be fine.
{{% /note %}}
Create a file called `basic_io.py` ("io" is short for input/output). In it, write a program
that displays a friendly greeting:

	$ python basic_io.py
	What is your name? kevin
	Go away kevin

<a href="#demo" class="btn btn-info" data-toggle="collapse">Show solution</a>
<div id="demo" class="collapse">
```python
# basic_io.py
name = input("What is your name? ")
print("Go away", name)
```

{{% tip %}}
See the first line that starts with a `#`? That's a "comment." Python will
ignore everything that comes after the `#`, so you can use them to write notes
to whoever is reading the code. Here, I've used a comment to tell you the name of the
file.
{{% /tip %}}
</div>
