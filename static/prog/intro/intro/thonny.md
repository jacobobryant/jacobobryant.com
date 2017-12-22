+++
title = "installing python"
subsections = ["introduction"]
subsections_weight = 30
date = "2016-12-28T03:15:42-06:03"
+++
In this course we'll use a program called Thonny to help us write
Python programs. You can [get it here](http://thonny.org). After
installing and running the program, you should get a window like this:

![blank Thonny](blank.png)

You can type code into the top box, and then the bottom box will show
the output of your progrom. Type `print('hello world')` into the top
box and then press the green circle/triangle button. You'll have to
save your program somewhere, but after that you should see output like
so:

![hello world](hello.png)



<!--
At the end of the day, computers only understand ones and zeros
(a.k.a. binary). At some point, any program you run must be converted
into binary. However, writing programs in binary is a real drag, so
instead we write them in various programming languages. Then we use
another program that automatically converts the stuff we type into
binary. For Python, this converter program is called the Python
interpreter. You must download and install it:

 - **Ubuntu Linux:** Type `sudo apt-get install python3` in the
   terminal.
 - **Windows:** Download and run the [Windows
   installer](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe) (but see the note below).
 - **OS X:** Download and run the [OS X installer](
   https://www.python.org/ftp/python/3.6.1/python-3.6.1-macosx10.6.pkg).

On Windows, make sure you check the box that says "Add Python 3.6 to
PATH":

![Python installer](screen.png)

Once you have it installed, open the command line interface and type `python
--version`. If you're
on Linux and it doesn't work, try `python3 --version`. You should get something
like this:

<pre>
$ <b>python --version</b>
Python 3.5.2
</pre>

{{% note %}}
If you are on Windows and you didn't check "Add Python 3.6 to PATH",
the `python` command won't be available. Instead you could type `py
--version`, or you could reinstall Python and make sure to check the
box this time.

Also, the `$` is my prompt. It's the equivalent of `C:\Users\jacob>`
on Windows. You can ignore it; you don't need to type it.
{{% /note %}}






Now that you have Python installed, I'll show you how to run a Python
program that I wrote. Download [this file](/files/hilo.py). Normally
when you download a program, you click on it to make it run
automatically. Instead of doing that, I'll show you how to run the
program from the command line.

Open the command line and
use the `cd` command to move to the same folder where you saved the
program. Type `python hilo.py` (or `py hilo.py`) to run the program. For
example, if the file was saved in `Downloads`, then you would use the
following commands:

<pre>
$ <b>cd Downloads</b>
$ <b>python hilo.py </b>
</pre>

After running those commands, you'll see this output:

```
I'm thinking of a number between 1 and 100, sucka
You have 7 guesses left.
Pick a number:
```

Good luck.

{{% tip %}}
Try pressing Control-C while you're playing the game. It will end the
current program without making you play to the end.
{{% /tip %}}

Now that you know how to run a Python program, the only thing left is
to learn how to make the programs in the first place (how hard could it be?).
In the next episode, you'll learn how to mess around with your first Python
commands.
-->
