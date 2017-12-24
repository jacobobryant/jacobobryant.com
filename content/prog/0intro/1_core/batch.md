+++
title = "batch mode"
date = "2016-12-28T03:15:42-07:03"
subsections = [ "core" ]
subsections_weight = 3
draft = true
+++
("Batch" means "non-interactive.")

In this section, you will write your Python commands in a text file instead
of typing them into the Python shell. You'll need a good text editor for that. If you're
on Windows, the default text editor is Notepad, a terrible editor. Instead, I recommend
[Notepad++](https://notepad-plus-plus.org/download/). If you're on Linux or OS
X, whatever the default is will probably be fine.

Open your text editor and type the line `print("hello world")`, like
so:

![hello world](hello.png)

Then save the file as `hello.py`.
On Windows, I recommend that you save the file in "Computer" &rarr; "Local
Disk (C:)" &rarr; "Users" &rarr; [your user name] &rarr; create a new folder
called "programs". So the location of the file will be
`C:\Users\YourUsername\programs\hello.py`.

Now open the command line and use `cd` to navigate to the directory
where you saved your program. If you're on Windows and you followed my
advice above, you can open a new command prompt and type `cd
programs`.

Once you're there, you can run your program with `python hello.py`:

<pre>
$ <b>python hello.py</b>
hello world
</pre>

You did it! Try making changes to the text file and re-running the
program (don't forget to save the text file each time).

The next page
contains your first programming challenge.
