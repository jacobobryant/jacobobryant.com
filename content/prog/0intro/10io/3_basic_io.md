+++
name = "basic io"
+++
Now we'll write that program we mentioned earlier. In Thonny, go to
"File" -> "Save as..." and then save the file as `basic_io.py` ("io"
is short for input/output). In the upper box, write some commands to
do the following:

 1. use `input` to get the user's name
 2. use `print` to display a friendly greeting

After you write the commands, running the program should give you
output like this:

<pre>
>>> %Run basic_io.py
What is your name? <b>kevin</b>
Go away kevin
</pre>

Good luck! I've provided a solution below, but try to write the
program without looking at it first. You may need to go back to the
`print`, `variables` or `input` pages to refresh your memory.

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

After you get that working, change your program into a Mad Libs
thang:

<pre>
>>> %Run basic_io.py
enter a name: <b>steve</b>
enter another name: <b>winnifred</b>
enter a noun: <b>large hadron collider</b>
enter another noun (plural): <b>salad</b>
enter yet another noun: <b>stopwatch</b>
enter a verb ending in -ing: <b>frollicking</b>

steve and winnifred ran up the large hadron collider
to fetch a pale of salad
steve fell down and broke his stopwatch
and winnifred came frollicking after
</pre>
